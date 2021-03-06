import os
import sys
import logging
import importlib.util
from pathlib import Path


async def load_plugins(plugin_name):
    path = Path(f"./SayuBot/plugins/{plugin_name}.py")
    name = "SayuBot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["SayuBot.plugins." + plugin_name] = load
    print("SayuBot has Imported " + plugin_name)
