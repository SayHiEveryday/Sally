import os , sys
from discord.ext import commands

def restart_bot(): 
    os.execv(sys.executable, ['python'] + sys.argv)

class res(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="res")
    async def restart(self,ctx):
        if ctx.author.id == 698851209032761384:
            await ctx.send("Restarting bot")
            restart_bot()
        else:
            await ctx.reply("Call to Reboot failed: Interactive authentication required")

async def setup(bot):
    await bot.add_cog(res(bot))