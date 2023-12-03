import discord
from discord.ext import commands
from utils.arg import bot


class ready(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print("name: " + bot.user.name)
        print("id: " + str(bot.user.id))
        activity = discord.Game(name="/help")
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        await bot.tree.sync()

async def setup(bot):
    await bot.add_cog(ready(bot))