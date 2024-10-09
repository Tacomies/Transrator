from os import getenv, makedirs
from dotenv import load_dotenv
from discord import Intents, Client, Message
from commands import match_command
from datetime import datetime

load_dotenv()
TOKEN = getenv('TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

cache_dir: str = "/home/karri/transrator_cache"
if cache_dir == "":
    print("Cache dir not defined")
    exit()

makedirs(cache_dir, exist_ok=True)

def log(username: str, message: str) -> None:
    print(f"{datetime.now()} {username} {message}")

@client.event
async def on_ready() -> None:
    print(f"{client.user} running!")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content

    if len(user_message) == 0:
           return

    if user_message[0] != "!":
        return

    log(username, user_message)
    
    params: list = user_message.split(" ")
        
    await match_command(params[0][1:], params[1:], message, client, cache_dir)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()



