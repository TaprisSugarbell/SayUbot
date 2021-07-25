import os
from .. import SayuBot
from telethon import events, Button


@SayuBot.on(events.NewMessage(outgoing=True, pattern=r"(.install|.i)"))
async def install(event):
    ok = await event.get_reply_message()
    if hasattr(ok, "media"):
        try:
            filename = ok.file.name
            if str(filename).split(".")[-1] == "py":
                media = ok.media.document
                print(filename)
                # print(os.listdir("./"))
                if f"{filename}" not in os.listdir("./SayuBot/plugins/"):
                    await SayuBot.download_file(media, "./SayuBot/plugins/" + filename)
                    await event.edit("Instalando...")
                    await SayuBot.disconnect()
                else:
                    os.unlink("./SayuBot/plugins/" + filename)
                    await SayuBot.download_file(media, "./SayuBot/plugins/" + filename)
                    await event.edit("Instalando...")
                    await SayuBot.disconnect()

        except AttributeError:
            pass
