import discord
import discord.ext
from discord.ext import commands
import random
from storage.arg import answer
from discord import app_commands

class eightball(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @app_commands.command(name="8ball" , description="Help decide a question")
    async def eightball_slash(self,interaction: discord.Interaction , question: str):
        num = random.randint(0,len(answer))


        await interaction.response.send_message(f"Question: **{question}**\nAnswer: `{answer[num]}` , <@{interaction.user.id}>")

    @commands.command(name="8ball")
    async def eightball_prefix(self,ctx ,*, question: str):
        num = random.randint(0,len(answer))

        await ctx.reply(f"Question: **{question}**\n Answer:`{answer[num]}` , <@{ctx.author.id}>")

    @eightball_prefix.error
    async def ball_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Missing Required Argument")

async def setup(bot):
    await bot.add_cog(eightball(bot))