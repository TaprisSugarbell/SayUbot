import os
import time
import logging
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Config
load_dotenv()
OWNER_ID = int(os.getenv("OWNER_ID"))
SESSION = str(os.getenv("SESSION"))
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

SayuBot = TelegramClient(StringSession(SESSION), API_ID, API_HASH).start()
# SayuBot = TelegramClient('SayUbot', API_ID, API_HASH).start()
bot = TelegramClient('SayuBot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
