# AI Amount Detection Backend

## 📖 Overview
This project is a FastAPI-based backend application developed as part of the **Plum SDE Intern Assignment**.  
It extracts and detects monetary amounts from text using OCR and text processing techniques.

The backend exposes a REST API that accepts text or files and returns extracted amount information in a structured format.

---

## 🚀 Features
- FastAPI-based REST API
- Extracts monetary amounts from text
- OCR support for text extraction
- Clean modular code structure
- Easy to run and test locally

---

## 🛠️ Tech Stack
- Python 3
- FastAPI
- Uvicorn
- OCR (Tesseract / text extraction logic)

---
## 📂 Project Structure
ai-amount-detection-backend/
│
├── app/
│ ├── main.py # FastAPI app & API endpoints
│ ├── ocr.py # OCR and text extraction logic
│ ├── processing.py # Amount detection & processing logic
│
└── requirements.txt # Project dependencies

Paste this under your Setup / Installation section.
How to Run
## ▶️ How to Run

### 1. Go to project folder
```bat
cd C:\Users\ganna\Desktop\ai-amount-detection-backend

2. Create virtual environment
python -m venv venv

3. Activate virtual environment
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run the server
uvicorn app.main:app --reload

6. Open API docs

http://127.0.0.1:8000/docs
CTRL + C
