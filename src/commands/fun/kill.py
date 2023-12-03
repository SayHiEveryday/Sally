import discord
from discord.ext import commands
import asyncio
from utils.arg import kill
import random
from discord import app_commands

class kill(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="kill" , description="Hate someone? Kill them!")
    async def kill_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.name}> killed themself")
            return
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.name}> killed robot but robot come back and working perfectly fine")
            return
        
        await interaction.response.defer()
        await asyncio.sleep(2)
        await interaction.followup.send(kill[random.randint(0,185)].replace("$mention" , f"<@{member.id}>").replace("$author" , f"<@{interaction.user.id}>"))

    @commands.command(name="kill")
    async def kill_prefix(self,ctx , member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> killed themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> killed robot but robot come back and working perfectly fine")
            return
        
        await ctx.send(kill[random.randint(0,185)].replace("$mention" , f"<@{member.id}>").replace("$author" , f"<@{ctx.author.id}>"))

    @kill_prefix.error
    async def kill_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Ok you're dead. Please mention someone else to kill.")


async def setup(bot):
    await bot.add_cog(kill(bot))