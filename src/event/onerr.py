import nextcord , json , os
from nextcord.ext import commands
from utils.run import bot
from utils.arg import owner


class onerr(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        global errorg
        errorg = error
        if len(str(error)) > 1500:
            firstpart, secondpart = error[:len(error)//2], error[len(error)//2:]
        if not secondpart:
            embed = nextcord.Embed(title="Command Error!" , description=f"```\n{error}\n```")
            a = await bot.fetch_user(owner)
            a.send(embed=embed)
        else:
            embed = nextcord.Embed(title="Command Error first part" , description=f"```\n{firstpart}\n```")
            embed2 = nextcord.Embed(title="Second part" , description=f"```\n{secondpart}\n```")
            a = await bot.fetch_user(owner)
            a.send(embeds=[embed , embed2])
        

def setup(bot):
    bot.add_cog(onerr(bot))