from SayuBot import SayuBot
from telethon import events, Button


@SayuBot.on(events.NewMessage(pattern=r"\.rt"))
async def restart(event):
    await SayuBot.disconnect()




