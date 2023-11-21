import nextcord
import nextcord.ext
from nextcord.ext import commands
import random
from utils.arg import answer

class eightball(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="8ball" , description="Help decide a question")
    async def eightball_slash(self,interaction: nextcord.Interaction , question: str):
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

def setup(bot):
    bot.add_cog(eightball(bot))