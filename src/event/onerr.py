import discord , json , os
from discord.ext import commands
from utils.arg import bot
from utils.arg import owner


class onerr(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            return
        elif isinstance(error,commands.CommandNotFound):
            return
        else:
            global errorg
            errorg = error
            if len(str(error)) > 1500:
                firstpart, secondpart = error[:len(error)//2], error[len(error)//2:]
            try:
                secondpart
            except NameError:
                embed = discord.Embed(title="Command Error!" , description=f"Command: {ctx.command}\nGuild name: {ctx.guild.name}\nGuild id: {ctx.guild.id}\n```\n{error}\n```")
                a = await bot.fetch_user(owner)
                await a.send(embed=embed)
            else:
                embed = discord.Embed(title="Command Error first part" , description=f"```\n{firstpart}\n```")
                embed2 = discord.Embed(title="Second part" , description=f"Command: {ctx.command}\nGuild name:{ctx.guild.name}\nGuild id: {ctx.guild.id}\n```\n{secondpart}\n```")
                a = await bot.fetch_user(owner)
                await a.send(embeds=[embed , embed2])
        

async def setup(bot):
    await bot.add_cog(onerr(bot))