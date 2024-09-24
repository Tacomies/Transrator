from deep_translator import GoogleTranslator
from langdetect import detect


def get_language(text: str) -> str | None:
    result: str | None = None

    try:
        result = detect(text)
    except Exception as err:
        print(f"Couldn't detect language'{err}")

    return result

def translate(text: str, language: str) -> str | None:
    result: str | None = None

    try:
        result = GoogleTranslator(source="auto", target=language).translate(text)
    except Exception as err:
        if "no support" in str(err).lower():
            print(f"Language {language} not supported")
            return result

        print(f"Couldn't translate: {err}")
        
    return result

