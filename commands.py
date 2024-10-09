from os import path, remove
from langtools import translate
from audiotools import to_mp3
from discord import Message, Client, File
from discordtools import send_message, get_text
from time import time
from imagetools import get_text as get_text_from_image
from webtools import get_image

async def translate_message(params: list, message: Message, client: Client):
    result: str | None = None
    link: str = params[-1]
    language: str = params[0]

    text: str | None = await get_text(link, client)
    
    if not text:
        print("Couldn't fetch message'")
        return

    try:
        result = translate(text, language)
    except Exception as err:
        print(f"Couldn't translate {err}")

    if not result:
        result = "Couldn't translate"
    
    await send_message(message, result)

async def translate_image(params: list, message: Message, client: Client):
    valid_formats: list = ["jpeg", "jpg", "png", "bmp", "tiff", "tif", "gif", "webp"]
    language: str = params[0]
    link: str = params[-1]
    text: str = get_text_from_image(get_image(link, valid_formats))
    result: str | None = None

    if not text:
        print("No text found in image")
        return

    try:
        result = translate(text, language)
    except Exception as err:
        print(f"Couldn't translate {err}")

    if not result:
        result = "Couldn't translate"
    
    await send_message(message, result)

    
async def speech(params: list, message: Message, client: Client, cache_dir: str) -> None:
    link: str = params[0]
    
    text: str | None = await get_text(link, client)
    
    if not text:
        print("Couldn't fetch message'")
        return
        
    identifier: str = str(int(time()))
    filename: str = cache_dir + identifier 

    try:
        to_mp3(text, filename)
    except Exception as err:
        print(f"Failed to make audio {err}")
        await send_message(message, "Couldn't convert")
        return

    if path.isfile(filename) == False:
        return
    
    audio: File | None = None
    try:
        audio = File(filename, filename=f"{identifier}.mp3")
    except Exception as err:
        print(err)
        
    remove(filename)

    await send_message(message, audio)
        
    
async def match_command(command: str, params: list, message: Message, client: Client, cache_dir: str) -> None:
    if command == "translate":
        await translate_message(params, message, client)
    elif command == "speech":
        await speech(params, message, client, cache_dir)
    elif command == "image":
        await translate_image(params, message, client)
    else:
        print(f"{command} is not a valid command")
