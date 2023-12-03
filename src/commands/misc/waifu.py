from discord.ext import commands
from utils.api.waifu import wai

class waifu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def waifu(self,ctx: commands.Context):
        await ctx.reply(wai())

async def setup(bot):
    await bot.add_cog(waifu(bot))