import discord
from discord import app_commands
from discord.ext import commands
import psutil , platform , cpuinfo , os , distro,subprocess ,string ,time
from utils.handler.logcmd import *

def stats_forsys(ctx):
    start_time = time.time()
    ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    try:
        cpu = cpuinfo.get_cpu_info()['brand_raw']
    except:
        a = subprocess.run("neofetch --off --stdout --color_blocks off | grep CPU", shell=True, capture_output=True, text=True)
        a = str(a.stdout)
        b = a.replace("CPU:" , "").replace("\n","")
        cpu = b
    u = subprocess.run("python3 -m uptime", shell=True, capture_output=True, text=True)
    d = str(u.stdout)
    embed = discord.Embed(title="**Stats**" , colour=discord.Color.dark_embed())
    embed.add_field(name="Host Infomation" , value=f"```\nCPU: {cpu}\nRam: {ram}\n```" , inline=False)
    embed.add_field(name="OS Infomation" , value=f"```Platform: {platform.system()}\nOS: {distro.name(pretty=True)}\nKernel: {str(platform.uname().release)}\nArchitecture: {platform.machine()}\n```" , inline=False)
    embed.add_field(name="Bot Infomation" , value=f"```\n{d}Python Version: {platform.python_version()}\nLibary: discord.py {discord.__version__}\nRam usage: {round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)} MB\n```" , inline=False)
    embed.set_footer(text=f"Execution took {round((time.time() - start_time) * 1000)} ms",icon_url=ctx.display_avatar.url)
    return embed

class sysinfo(commands.Cog):
    def __init__(self, client):
        self.client = client    

    @commands.command(name="stats")
    async def _sysinfo(self,ctx):
        await ctx.reply(embed=stats_forsys(ctx=ctx.author) , mention_author=False)
    
    @app_commands.command(name="stats",description="show host systeminfo")
    @app_commands.describe(ephemeral="make the result visable to other?")
    async def s_sysinfo(self,interaction:discord.Interaction , ephemeral:bool=True):
        await interaction.response.send_message(embed=stats_forsys(ctx=interaction.user),ephemeral=ephemeral)


async def setup(bot):
    await bot.add_cog(sysinfo(bot))
