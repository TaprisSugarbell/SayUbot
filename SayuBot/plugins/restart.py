import os
import heroku3
from dotenv import load_dotenv
from telethon import events, Button
from SayuBot import SayuBot, OWNER_ID

# ADMINS and COMMANDS
load_dotenv()
APP_NAME = os.getenv("APP_NAME")
# ADMINS_STR = os.getenv("ADMINS")
HEROKU_API = os.getenv("HEROKU_API")
CLIENT = heroku3.from_key(HEROKU_API)
# ADMINS = [int(i) for i in ADMINS_STR.split(" ")]


@SayuBot.on(events.NewMessage(pattern=r"\.rt"))
async def restart(event):
    print(event)
    user = event.sender_id
    if user == OWNER_ID:
        await event.edit(f"Reiniciando {APP_NAME}...")
        app = CLIENT.app(APP_NAME)
        app.restart()


@SayuBot.on(events.NewMessage(pattern=r"\.rc"))
async def restart(event):
    print(event)
    user = event.sender_id
    if user == OWNER_ID:
        await SayuBot.disconnect()


