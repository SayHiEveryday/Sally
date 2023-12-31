import discord,json
import discord.ext
from discord.ext import commands
from utils.api.getsysinfo import getSystemInfo



class sysinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="sysinfo")
    async def sysinfo(self,ctx):

        if ctx.author.id == 698851209032761384:
            a = json.loads(getSystemInfo())
            embed = discord.Embed(title="host sysinfo" , description=f"platform: {a['platform']} \nplatform version: {a['platform-version']}\narchitecture: {a['architecture']}\nhostname: {a['hostname']}\n ip: {a['ip-address']}\nmac-address: {a['mac-address']}\nprocessor {a['processor']}\nram: {a['ram']}")
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("no perm")

async def setup(bot):
    await bot.add_cog(sysinfo(bot))