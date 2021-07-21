import glob
import logging
import asyncio
from pathlib import Path
from SayuBot import SayuBot, bot
from SayuBot.helper.utils import load_plugins

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
loop = asyncio.get_event_loop()


async def loadPlugins():
    path = "./plugins/*.py"
    files = glob.glob(path)
    print(files)
    for name in files:
        print(name)
        with open(name) as a:
            print(a.name)
            patt = Path(a.name)
            plugin_name = patt.stem
            await load_plugins(plugin_name.replace(".py", ""))

    print("Se ha iniciado!")
    print("Disfrutalo! Sigueme en @SayuCodez")


async def SayuStart():
    print("Iniciando...")
    await SayuBot.start()
    await bot.connect()
    await loadPlugins()
    await SayuBot.run_until_disconnected()
    await bot.disconnect()
    print("Desconectandose...")
    return 0


if __name__ == "__main__":
    s = loop.run_until_complete(SayuStart())
    while s == 0:
        s = loop.run_until_complete(SayuStart())
