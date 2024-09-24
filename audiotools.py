from gtts import gTTS
from langtools import get_language

def to_speech(text: str) -> gTTS | None:
    language: str | None = get_language(text)

    if not language:
        return 
    
    speech: gTTS | None = None

    try:
        speech = gTTS(text=text, lang=language, slow=False)
    except Exception as err:
        print(err)

    return speech

def to_mp3(text: str, filename: str) -> str | None:
    speech: gTTS | None = to_speech(text)

    if not speech:
        print("Couldn't convert to speech")
        return

    try:
        speech.save(filename)
    except Exception as err:
        print("Couldn't save audio {err}")

    return


