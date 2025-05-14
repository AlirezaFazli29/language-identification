import gc
from fastapi import FastAPI
from .schemas import Request
from ..core.lang import LangDetector
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse


lang_detector = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager for initializing and cleaning up global dependencies.

    This function sets up the `lang_detector` instance of `LangDetector` on application startup,
    and ensures it is deleted and garbage-collected on shutdown.

    Args:
        app (FastAPI): The FastAPI app instance.

    Yields:
        None: Allows FastAPI to continue with the startup process.
    """
    global lang_detector
    lang_detector = LangDetector()
    yield
    del lang_detector
    lang_detector = None
    gc.collect()


app = FastAPI(
    title = "Language Detector",
    lifespan = lifespan,
)


@app.get(
    path = "/",
    tags = [
        "Language",
    ],
)
async def root():
    """
    Root endpoint for the service.

    This endpoint serves as a basic health check to verify if the service is up and running.

    Returns:
        JSONResponse: A JSON response containing service status.
    """
    return JSONResponse(
        {
            "message": "Service is up and running",
        }
    )


@app.post(
    path = "/detect/",
    tags = [
        "Language",
    ],
)
async def detect_lang(
    request: Request,
):
    """
    Endpoint to detect the language of a given text.

    This endpoint accepts a POST request with a body containing the text.
    It returns the detected language code and the confidence score.

    Args:
        request (Request): The FastAPI request object containing the text to be analyzed.

    Returns:
        JSONResponse: A JSON response containing the detected language and confidence score.
    """
    text = request.text
    lang, conf = lang_detector.detect_lang(text)
    return JSONResponse(
        {
            "detected-language": lang,
            "confidence": conf,
        }
    )


@app.get(
    path = "/lang-list/",
    tags = [
        "Language",
    ],
)
async def list_lang():
    """
    Endpoint to list all the supported languages by the language detection model.

    This endpoint returns a list of supported language codes from the FastText model.

    Returns:
        JSONResponse: A JSON response containing a list of supported language codes.
    """
    res = lang_detector.get_supported_languages()
    return JSONResponse(
        {
            "supported-languages": res,
        }
    )