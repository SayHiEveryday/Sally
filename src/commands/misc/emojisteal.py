import discord
from discord.ext import commands
from discord import app_commands

class emojisteal(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="emojisteal",aliases=["emo","emoji"])
    async def steal_prefix(self,ctx , emoji: discord.PartialEmoji):
        await ctx.reply(emoji.url)

    @steal_prefix.error
    async def error(self,ctx,error):
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.reply("Please provide emoji to steal")

async def setup(bot):
    await bot.add_cog(emojisteal(bot))