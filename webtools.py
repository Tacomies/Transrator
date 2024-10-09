from requests import get
from PIL import Image
from io import BytesIO


def get_image(content_url: str, valid_formats: list):

    response = get(content_url)
    content_type: str | None = response.headers.get("Content-Type")
    
    if not content_type:
        raise TypeError(f"Couldn't make out fileformat")

    if content_type.lower().replace("image/", "") not in valid_formats:
        raise TypeError(f"Filetype {content_type} is not supported")

    image = Image.open(BytesIO(response.content))
    image.verify()

    return image


    





