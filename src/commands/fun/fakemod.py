import discord
from discord.ext import commands
import asyncio
import datetime
from discord import app_commands

class fakemod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="fakemod" , description="Fake moderation")
    @app_commands.describe(action="Select an action to moderate mention member")
    @app_commands.choices(action=[
        app_commands.Choice(name="ban" , value=0),
        app_commands.Choice(name="mute",value=1),
        app_commands.Choice(name="kick",value=2)
    ])
    async def fakemod(self,interaction: discord.Interaction,member: discord.Member,reason:str,action: discord.app_commands.Choice[int]):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"you can't fake {action} yourself",ephemeral=False)
            return
        if member.bot.real:
            await interaction.response.send_message(f"you can't fake {action} to a bot",ephemeral=False)
            return
        embed1 = discord.Embed(title=f"**{member.name} has been {action.name}!**" , description=f"With reason:{reason}",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed2 = discord.Embed(title=f"**You have been {action.name} from {interaction.guild.name}**",description=f"With reason: {reason}\n**THIS IS A JOKE**",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed3 = discord.Embed(title=f"**{member.name} have been {action.name} from {interaction.guild}**",description=f"With reason: {reason} \n**THIS IS A JOKE**",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed4 = discord.Embed(title=f"**You have been {action.name} from {interaction.guild.name}**",description=f"With reason: {reason}",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed1,ephemeral=False)
        msg = await interaction.original_response()
        msg2 = await member.send(embed=embed4)
        await asyncio.sleep(5)
        await msg.edit(embed=embed3)
        await msg2.edit(embed=embed2)

async def setup(bot):
    await bot.add_cog(fakemod(bot))
