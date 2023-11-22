import nextcord , json , os
from nextcord.ext import commands
from utils.run import bot
from utils.arg import owner


class onerr(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply("hey! missing required argument (this is global error handling)")
        else:
            global errorg
            errorg = error
            if len(str(error)) > 1500:
                firstpart, secondpart = error[:len(error)//2], error[len(error)//2:]
            try:
                secondpart
            except NameError:
                embed = nextcord.Embed(title="Command Error!" , description=f"Command: {ctx.command}\nGuild name: {ctx.guild.name}\nGuild id: {ctx.guild.id}\n```\n{error}\n```")
                a = await bot.fetch_user(owner)
                await a.send(embed=embed)
            else:
                embed = nextcord.Embed(title="Command Error first part" , description=f"```\n{firstpart}\n```")
                embed2 = nextcord.Embed(title="Second part" , description=f"Command: {ctx.command}\nGuild name:{ctx.guild.name}\nGuild id: {ctx.guild.id}\n```\n{secondpart}\n```")
                a = await bot.fetch_user(owner)
                await a.send(embeds=[embed , embed2])
        

def setup(bot):
    bot.add_cog(onerr(bot))