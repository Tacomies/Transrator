from pytesseract import image_to_string as img_to_str
from PIL import Image


def get_text(image) -> str:
    text: str = img_to_str(image)
    return text


