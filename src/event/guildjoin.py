import json , os , discord
from discord.ext import commands
from storage.arg import bot
import aiosqlite

class guildjoin(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        activity = discord.Game(name=f"/help | {len(bot.guilds)} Servers!")
        await bot.change_presence(status=discord.Status.idle, activity=activity)

        with open("storage/prefix.json" , "r") as f:
            prefix = json.load(f)

        prefix[str(guild.id)] = "s!"

        with open(os.path.dirname(__file__) + "/../storage/prefix.json" , "w") as f:
            json.dump(prefix , f)
        f.close()
        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            await db.execute(f"SELECT * FROM prefix WHERE guild = {str(guild.id)}")

async def setup(bot):
    await bot.add_cog(guildjoin(bot))
