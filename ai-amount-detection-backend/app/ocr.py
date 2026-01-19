import pytesseract
from PIL import Image
import re

# Tell Python where Tesseract OCR is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image: Image.Image) -> str:
    """
    Extract text from image using OCR
    """
    return pytesseract.image_to_string(image)

def extract_tokens(text: str):
    """
    Extract numeric tokens and currency hints
    """
    tokens = re.findall(r"\d+%?", text)
    currency = "INR" if any(x in text.lower() for x in ["inr", "rs", "₹"]) else "INR"
    return tokens, currency
