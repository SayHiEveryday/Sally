import os , json , asyncio
from utils.api.getsysinfo import getSystemInfo
from utils.handler.loadcogs import initial_extension
from utils.arg import bot , token

async def load():
    for extenstion in initial_extension:
        await bot.load_extension(extenstion)

asyncio.run(load())

if __name__ == "__main__":

    if json.loads(getSystemInfo())['platform'] == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    bot.run(token)