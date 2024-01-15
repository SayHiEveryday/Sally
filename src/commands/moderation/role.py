import discord
from discord.ext import commands
import time
from discord import app_commands

class roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    rolegroup = app_commands.Group(name="role",description="Roles utility")

    @rolegroup.command(name="add",description="add role to mentioned member")
    async def rolegroup_add(self,interaction: discord.Interaction,member: discord.Member,role: discord.Role):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("Hey! you don't have permission to execute this command",ephemeral=True)
            return
        if role in member.roles:
            await interaction.response.send_message(f"{member.mention} already have {role.mention}",ephemeral=True)
            return
        try:
            await member.add_roles(role)
            embed = discord.Embed(description=f"Added {role.mention} to {member.mention}",colour=0x3BA55C)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            if "404" in str(e):
                await interaction.response.send_message("Fail to add role, I can't add role that are higher or same level as me",ephemeral=True)
    
    @rolegroup.command(name="remove",description="remove role from mentioned member if there is")
    async def rolegroup_remove(self,interaction:discord.Interaction,member:discord.Member,role:discord.Role):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("Hey! you don't have permission to execute this command",ephemeral=True)
            return
        if role not in member.roles:
            await interaction.response.send_message(f"{member.mention} doesn't have {role.mention}",ephemeral=True)
            return
        try:
            await member.remove_roles(role)
            embed = discord.Embed(description=f"Removed {role.mention} from {member.mention}",colour=0xED4245)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            if "404" in str(e):
                await interaction.response.send_message("Fail to remove role, I can't remove role that are higher or same level as me",ephemeral=True)

async def setup(bot):
    await bot.add_cog(roles(bot))