from discord.ext import commands
import discord
from discord import app_commands
from utils.handler.logcmd import *
class impersonate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="impersonate" , description="impersonate someone with usage of webhook")
    @app_commands.describe(member="Member to impersonate",msg="Message to send")
    @app_commands.checks.cooldown(1,30,key=lambda i: (i.guild_id,i.user.id))
    async def impersonate_command(self,interaction: discord.Interaction , member: discord.Member , msg: str):
        if "@everyone" in msg:
            await interaction.response.send_message("you can not ping everyone with impersonate commands",ephemeral=True)
            return
        if "@here" in msg:
            await interaction.response.send_message("you can not ping here with impersonate commands",ephemeral=True)
            return
        if "<@&" in msg:
            await interaction.response.send_message("you can not ping role with impersonate commands",ephemeral=True)
            return
        
        await interaction.response.send_message(content="Sending message please wait",ephemeral=True)
        hook = await interaction.channel.create_webhook(name=member.display_name,reason=f"impersonate command on sally bot (created by {interaction.user.name})")
        await hook.send(content=msg,avatar_url=member.display_avatar.url)
        await hook.delete()
        a = await interaction.original_response()
        await a.edit(content=f"message sent! => {a.jump_url}")

    @impersonate_command.error
    async def err(self,interaction: discord.Interaction,error: app_commands.AppCommandError):
        if isinstance(error,app_commands.CommandOnCooldown):
            await interaction.response.send_message(error,ephemeral=True)
            return
        else:
            embed = discord.Embed(
                title="Please report this to the developer (username = sa.l)",
                description=f"```\n{error}\n```",
                colour=discord.Color.random()
            )
            await interaction.response.send_message(content="https://discord.gg/jWkknghvaz",embed=embed , ephemeral=True)

async def setup(bot):
    await bot.add_cog(impersonate(bot))
