import nextcord
from nextcord.ext import commands
import asyncio
from utils import api
import random

class kill(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="kill" , description="Hate someone? Kill them!")
    async def kill_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.name}> killed themself")
            return
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.name}> killed robot but robot come back and working perfectly fine")
            return
        
        await interaction.response.defer()
        await asyncio.sleep(2)
        await interaction.followup.send(api.kill[random.randint(1,185)].replace("$mention" , f"<@{member.id}>").replace("$author" , f"<@{interaction.user.id}>"))

    @commands.command(name="kill")
    async def kill_prefix(self,ctx , member: nextcord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> killed themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> killed robot but robot come back and working perfectly fine")
            return
        
        await ctx.send(api.kill[random.randint(1,185)].replace("$mention" , f"<@{member.id}>").replace("$author" , f"<@{ctx.author.id}>"))

    @kill_prefix.error
    async def kill_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Ok you're dead. Please mention someone else to kill.")


def setup(bot):
    bot.add_cog(kill(bot))