import discord , os
import discord.ext
from discord.ext import commands
import json
import datetime
from utils.handler.loadcogs import initial_extension
from discord import app_commands
from utils.handler.logcmd import *
path = os.path.dirname(__file__) + "/../salonly/"
class prefixbutton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label=f"Total command is {len(initial_extension) - len(os.listdir(path=path)) + 1}", style=discord.ButtonStyle.primary, custom_id="total" , disabled=True)
    async def total(self, button: discord.Button, interaction: discord.Interaction):
        pass

class helpcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="help" , description="View all commands")
    async def help_slash(self,interaction: discord.Interaction):
        with open(os.path.dirname(__file__) + "/../../storage/prefix.json" , "r") as f:
            prefix = json.load(f)
        
        helpembed = discord.Embed(title=f"**Hey {interaction.user.name}!**", description=f"**you can find some useful link here**\n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally) \n<:idk:1171141480539246653> **List of all commands:**\n[app.gitbook.com](https://sayhis-organization.gitbook.io/sally-book/)\n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {prefix[str(interaction.guild.id)]}**",colour=0x5865F2,timestamp=datetime.datetime.now())
        await interaction.response.send_message(embed=helpembed.set_author(name=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url) , view=prefixbutton())

    @commands.command(name="help")
    async def help_prefix(self,ctx):

        with open(os.path.dirname(__file__) + "/../../storage/prefix.json" , "r") as f:
            prefix = json.load(f)

        helpembed = discord.Embed(title=f"**Hey {ctx.author.name}!**", description=f"**you can find some useful link here**\n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally) \n<:idk:1171141480539246653> **List of all commands:**\n[app.gitbook.com](https://sayhis-organization.gitbook.io/sally-book/)\n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {prefix[str(ctx.guild.id)]}**",colour=0x5865F2,timestamp=datetime.datetime.now())
        await ctx.send(embed=helpembed.set_author(name=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url) , view=prefixbutton())

async def setup(bot):
    await bot.add_cog(helpcmd(bot))