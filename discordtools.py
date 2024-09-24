from discord import Message, File, Client
import re

MESSAGE_LINK_RE = re.compile(r"https://discord(?:app)?.com/channels/(\d+)/(\d+)/(\d+)")


async def send_message(message, response: str | File):
    try:
        if type(response) == File:
            await message.channel.send(file=response)
            return

        await message.channel.send(response)
    except Exception as err:
        print(f"Failed to send response {err}")

async def get_text(link: str, client: Client) -> str | None:
    match = MESSAGE_LINK_RE.match(link)
    if not match:
        return "Invalid message link!"

    guild_id = int(match.group(1))
    channel_id = int(match.group(2))
    message_id = int(match.group(3))
   
    guild = client.get_guild(guild_id)
    if not guild:
        return "Guild not found!"

    channel = guild.get_channel(channel_id)
    if not channel:
        return "Channel not found!"

    message: Message | None = None
    
    try:
        message = await channel.fetch_message(message_id)
    except Exception as err:
        print(f"Couldn't fetch message {err}")

    if message:
        return str(message.content) 

    return None
 
