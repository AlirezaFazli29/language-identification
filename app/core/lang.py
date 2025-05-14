import fasttext
from typing import Tuple, List
from functools import lru_cache


class LangDetector:
    """
    Language detection utility using Facebook's FastText language identification model.
    """

    def __init__(
            self,
            model_pth: str = "app/core/model/lid.176.bin",
    ):
        """
        Initialize the language detector by loading the FastText model.

        Args:
            model_pth (str): Path to the pre-trained FastText language identification model.
        """
        self.model = fasttext.load_model(path=model_pth)

    def detect_lang(
            self,
            text: str,
    ) -> Tuple:
        """
        Detect the language of a given text string.

        Args:
            text (str): Input text to classify.

        Returns:
            Tuple[str, float]: Detected language code (e.g., 'en') and confidence score (0.0–1.0).
        """
        predictions = self.model.predict(text=text)
        label = predictions[0][0]
        confidence = predictions[1][0]
        language_code = label.replace('__label__', '')
        return language_code, confidence

    @classmethod
    @lru_cache
    def get_supported_languages(
            cls,
            model_pth: str = "app/core/model/lid.176.bin",
    ) -> List:
        """
        Return the list of language codes supported by the model.

        This method caches the result using lru_cache to avoid repeated model loading.

        Args:
            model_pth (str): Path to the FastText model file.

        Returns:
            List[str]: List of ISO 639-1 or related language codes (e.g., ['en', 'fr', 'de', ...]).
        """
        model = fasttext.load_model(model_pth)
        labels = model.get_labels()
        return [label.replace("__label__", "") for label in labels]
