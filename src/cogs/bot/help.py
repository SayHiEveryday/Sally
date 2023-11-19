import nextcord , os
import nextcord.ext
from nextcord.ext import commands
import json
import datetime

class prefixbutton(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label=f"Total command is 28", style=nextcord.ButtonStyle.primary, custom_id="total" , disabled=True)
    async def total(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await interaction.send("hm")

class helpcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="help" , description="View all commands")
    async def help_slash(self,interaction: nextcord.Interaction):
        with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
            prefix = json.load(f)
        
        helpembed = nextcord.Embed(title=f"**Hey {interaction.user.name}!**", description=f"**you can find some useful link here**\n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally) \n<:idk:1171141480539246653> **List of all commands:**\n[app.gitbook.com](https://app.gitbook.com/o/gjaaRV2t2oRnQQnonm2i/s/XJIXhFgtdHOqdU490j5L/)\n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {prefix[str(interaction.guild.id)]}**",colour=0x5865F2,timestamp=datetime.datetime.now())
        await interaction.response.send_message(embed=helpembed.set_author(name=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url) , view=prefixbutton())

    @commands.command(name="help")
    async def help_prefix(self,ctx):

        with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
            prefix = json.load(f)

        helpembed = nextcord.Embed(title=f"**Hey {ctx.author.name}!**", description=f"**you can find some useful link here**\n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally) \n<:idk:1171141480539246653> **List of all commands:**\n[app.gitbook.com](https://app.gitbook.com/o/gjaaRV2t2oRnQQnonm2i/s/XJIXhFgtdHOqdU490j5L/)\n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {prefix[str(ctx.guild.id)]}**",colour=0x5865F2,timestamp=datetime.datetime.now())
        await ctx.send(embed=helpembed.set_author(name=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url) , view=prefixbutton())

def setup(bot):
    bot.add_cog(helpcmd(bot))