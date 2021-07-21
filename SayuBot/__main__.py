import glob
import logging
import asyncio
from pathlib import Path
from utils import load_plugins
from SayuBot import SayuBot, bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
loop = asyncio.get_event_loop()


def loadPlugins():
    path = "./plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    print("Se ha iniciado!")
    print("Disfrutalo! Sigueme en @SayuCodez")


async def SayuStart():
    print("Iniciando...")
    await SayuBot.start()
    await bot.connect()
    loadPlugins()
    await SayuBot.run_until_disconnected()
    await bot.disconnect()
    print("Desconectandose...")
    return 0


if __name__ == "__main__":
    s = loop.run_until_complete(SayuStart())
    while s == 0:
        s = loop.run_until_complete(SayuStart())
