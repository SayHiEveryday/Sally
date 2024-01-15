from discord.ext import commands
from utils.api.waifu import wai
import json , discord,requests,time
from utils.handler.logcmd import *
from discord import app_commands

class waifu_cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def waifu(self,ctx: commands.Context):
        if ctx.guild.id == 893725839236157450: return;
            
        start_time = time.time()
        try:
            if ctx.channel.nsfw:
                waifunsfw = json.loads(wai(nsfw="True"))
                cnf = str(waifunsfw['color'])
                cnf = cnf.replace("#","0x")
                cnf = int(cnf,16)
                embed1 = discord.Embed(description=f"Source: {waifunsfw['source']}\n Artist: {waifunsfw['artist']}", colour=cnf).set_image(url=waifunsfw['url']).set_footer(text=f"Execution took {round(time.time() - start_time)} second(s)",icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=embed1)
            else:
                waifusfw = json.loads(wai(nsfw="False"))
                csf = str(waifusfw['color'])
                csf = csf.replace("#","0x")
                csf = int(csf,16)
                embed2 = discord.Embed(description=f"Source: {waifusfw['source']}\n Artist: {waifusfw['artist']}" , colour=csf).set_image(url=waifusfw['url']).set_footer(text=f"Execution took {round(time.time() - start_time)} second(s)",icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=embed2)
        except Exception as e:
            await ctx.reply(str(e))

    @commands.command(name="waifu2")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def testcmd(self,ctx:commands.Context,arg:str="waifu"):
        if ctx.guild.id == 893725839236157450: return;
        
        if ctx.channel.nsfw:
            re = requests.get(f"https://api.waifu.pics/nsfw/{arg}")
            await ctx.reply(content=re.json()['url'],mention_author=False)
        else:
            re = requests.get(f"https://api.waifu.pics/sfw/{arg}")
            await ctx.reply(content=re.json()['url'],mention_author=False)

    @app_commands.command(name="nsfw",description="Provide nsfw image base on option")
    @app_commands.describe(types="Select to return an image base on it")
    @app_commands.choices(types=[
        app_commands.Choice(name="hass", value="hass"),
        app_commands.Choice(name="hmidriff", value="hmidriff"),
        app_commands.Choice(name="pgif", value="pgif"),
        app_commands.Choice(name="4k",value="4k"),
        app_commands.Choice(name="hentai",value="hentai"),
        app_commands.Choice(name="holo",value="holo"),
        app_commands.Choice(name="hneko",value="hneko"),
        app_commands.Choice(name="neko",value="neko"),
        app_commands.Choice(name="hkitsune",value="hkitsune"),
        app_commands.Choice(name="kemonomimi",value="kemonomimi"),
        app_commands.Choice(name="anal",value="anal"),
        app_commands.Choice(name="hanal",value="hanal"),
        app_commands.Choice(name="gonewild",value="gonewild"),
        app_commands.Choice(name="ass",value="ass"),
        app_commands.Choice(name="pussy",value="pussy"),
        app_commands.Choice(name="thigh",value="thigh"),
        app_commands.Choice(name="hthigh",value="hthigh"),
        app_commands.Choice(name="gah",value="gah"),
        app_commands.Choice(name="paizuri",value="paizuri"),
        app_commands.Choice(name="tentacle",value="tentacle"),
        app_commands.Choice(name="boobs",value="boobs"),
        app_commands.Choice(name="hboobs",value="hboobs")
        ])
    async def waifu_s(self,interaction: discord.Interaction,types: app_commands.Choice[str] , private:bool=True):
        if interaction.guild.id == 893725839236157450: return;     
        
        if not interaction.channel.nsfw:
            if private == False:
                await interaction.response.send_message("Please use this command only in nsfw channel else you need to keep private option to true",ephemeral=True)
                return
        start_time = time.time()
        r = requests.get(f"https://nekobot.xyz/api/image?type=" + str(types.value))
        f = json.loads(r.text)
        embed = discord.Embed(colour=f['color'])
        embed.set_footer(text=f"Execution took {round(time.time() - start_time)} second(s)",icon_url=interaction.user.display_avatar.url)
        embed.set_image(url=f['message'])
        await interaction.response.send_message(embed=embed,ephemeral=private)
async def setup(bot):
    await bot.add_cog(waifu_cog(bot))
