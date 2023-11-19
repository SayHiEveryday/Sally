import nextcord
from nextcord.ext import commands

class emojisteal(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="emojisteal")
    async def steal_prefix(self,ctx , emoji: nextcord.PartialEmoji):
        await ctx.reply(emoji.url)

    @steal_prefix.error
    async def error(self,ctx,error):
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.reply("Please provide emoji to steal")

def setup(bot):
    bot.add_cog(emojisteal(bot))