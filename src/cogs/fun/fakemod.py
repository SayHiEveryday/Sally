import nextcord
from nextcord.ext import commands
import asyncio
import datetime

class fakemod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="fakemod" , description="Fake moderation")
    async def fakemod(self,interaction: nextcord.Interaction,member: nextcord.Member,reason:str,action = nextcord.SlashOption(name="action",description="Mod type",choices=["ban","mute","kick"],required=True)):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"you can't fake {action} yourself",ephemeral=False)
            return
        if member.bot.real:
            await interaction.response.send_message(f"you can't fake {action} to a bot",ephemeral=False)
            return
        embed1 = nextcord.Embed(title=f"**{member.name} has been {action}!**" , description=f"With reason:{reason}",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed2 = nextcord.Embed(title=f"**You have been {action} from {interaction.guild.name}**",description=f"With reason: {reason}\n**THIS IS A JOKE**",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed3 = nextcord.Embed(title=f"**{member.name} have been {action} from {interaction.guild}**",description=f"With reason: {reason} \n**THIS IS A JOKE**",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed4 = nextcord.Embed(title=f"**You have been {action} from {interaction.guild.name}**",description=f"With reason: {reason}",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        msg = await interaction.response.send_message(embed=embed1,ephemeral=False)
        
        msg2 = await member.send(embed=embed4)
        await asyncio.sleep(5)
        await msg.edit(embed=embed3)
        await msg2.edit(embed=embed2)

def setup(bot):
    bot.add_cog(fakemod(bot))
