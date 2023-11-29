from nextcord.ext import commands
from utils.api.waifu import wai
class waifu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def waifu(self,ctx: commands.Context):
        await ctx.reply(wai())

def setup(bot):
    bot.add_cog(bot)