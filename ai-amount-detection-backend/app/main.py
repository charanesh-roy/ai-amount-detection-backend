from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import List
from PIL import Image
import io

from app.ocr import extract_text_from_image, extract_tokens
from app.processing import normalize_tokens, classify_amounts

app = FastAPI(title="AI-Powered Amount Detection Backend")


# ---------- REQUEST MODELS ----------

class ClassifyRequest(BaseModel):
    text: str
    amounts: List[int]


class FinalRequest(BaseModel):
    text: str
    raw_tokens: List[str]


# ---------- ENDPOINTS ----------

@app.post("/extract")
async def extract(
    text: str = Form(None),
    image: UploadFile = File(None)
):
    if image:
        image_bytes = await image.read()
        img = Image.open(io.BytesIO(image_bytes))
        extracted_text = extract_text_from_image(img)
    else:
        extracted_text = text or ""

    tokens, currency = extract_tokens(extracted_text)

    if not tokens:
        return {
            "status": "no_amounts_found",
            "reason": "document too noisy"
        }

    return {
        "raw_tokens": tokens,
        "currency_hint": currency,
        "confidence": 0.74
    }


@app.post("/normalize")
async def normalize(raw_tokens: List[str]):
    normalized, confidence = normalize_tokens(raw_tokens)

    if not normalized:
        return {"status": "normalization_failed"}

    return {
        "normalized_amounts": normalized,
        "normalization_confidence": confidence
    }


@app.post("/classify")
async def classify(req: ClassifyRequest):
    classified, confidence = classify_amounts(req.text, req.amounts)

    return {
        "amounts": classified,
        "confidence": confidence
    }


@app.post("/final")
async def final(req: FinalRequest):
    normalized, _ = normalize_tokens(req.raw_tokens)
    classified, _ = classify_amounts(req.text, normalized)

    return {
        "currency": "INR",
        "amounts": [
            {
                "type": item["type"],
                "value": item["value"],
                "source": f"text: '{item['type'].replace('_', ' ').title()} {item['value']}'"
            }
            for item in classified
        ],
        "status": "ok"
    }
