import discord 
from discord import app_commands
from discord.ext import commands

class onerr(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_command_error(self,ctx: commands.Context,error):
        if isinstance(error,commands.MissingRequiredArgument):
            return
        elif isinstance(error,commands.CommandNotFound):
            return
        elif isinstance(error,commands.CommandOnCooldown):
            await ctx.reply(error)
            return
        elif isinstance(error,commands.BadArgument):
            await ctx.reply(error)
            return
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(error)
            return
        else:
            embed = discord.Embed(
                title="Please report this to the developer (username = sa.l)",
                description=f"```\n{error}\n```",
                colour=discord.Color.random()
            )
            await ctx.reply(embed=embed)
async def setup(bot):
    await bot.add_cog(onerr(bot))
