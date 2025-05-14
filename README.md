# 🌍 FastText Language Detector API

RESTful FastAPI service for language detection using Facebook's [FastText](https://fasttext.cc/) pre-trained model (`lid.176.bin`). Detects over 170 languages with high accuracy.

---

## 📁 Project Structure

```
.
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── lang.py
│   │   └── model
│   │       └── lid.176.bin
│   └── main.py
├── .dockerignore
├── .gitignore
├── dev.ipynb
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── structure.txt

```

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd language-identification
```

### 2. Download the model

You **must** download the FastText model manually:

```bash
mkdir -p app/core/model/
wget -O app/core/model/lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
```

### 3. Run with Docker

```bash
docker compose build
```

Service will be available at:  
`http://localhost:8080`

---

## 🧪 API Endpoints

### Health Check

```http
GET /
```

**Response:**
```json
{ "message": "Service is up and running" }
```

---

### Detect Language

```http
POST /detect/
```

**Request Body:**
```json
{ "text": "Bonjour tout le monde" }
```

**Response:**
```json
{
  "detected-language": "fr",
  "confidence": 0.9998
}
```

---

### Supported Languages

```http
GET /lang-list/
```

**Response:**
```json
{
  "supported-languages": ["en", "fr", "de", ..., "zu"]
}
```

---

## ⚙️ Dev Setup (Local)

1. Create a virtualenv:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

2. Install deps:
   ```bash
   pip install -r requirements.txt
   ```

3. Run:
   ```bash
   python -m app.main
   ```

---

## 📝 Notes

- Requires **FastText** C++ extensions, so build tools (`build-essential`, `gcc`, `python3-dev`) are needed in your Docker image or local env.
- No model file included. You must download `lid.176.bin` yourself.
- Uses FastAPI’s async lifespan to load the model once at startup.

---

## 📄 License

MIT. Do whatever you want, just don’t be a jerk.
