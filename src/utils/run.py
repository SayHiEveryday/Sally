import os , json
from utils import api
from utils.handler.loadcogs import initial_extension
from utils.arg import bot , token

def start():
    for extenstion in initial_extension:
        bot.load_extension(extenstion)
    if json.loads(api.getSystemInfo())['platform'] == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    bot.run(token)
