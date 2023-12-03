import discord
from discord.ext import commands
import asyncio
from discord import app_commands

class role(commands.Cog):
    def __init__(self, client):
        self.client = client

    role_slash = app_commands.Group(name="role" ,description="Role utility" , default_permissions=discord.Permissions.manage_roles)

    @role_slash.command(name="all" , description="add a role to all the member in the guild")
    async def role_slash_all(self,interaction: discord.Interaction , role: discord.Role):
        try:
            guild = interaction.guild
            message = await interaction.response.send_message(embed=discord.Embed(description=f"**Status:** adding role to {guild.member_count} Will take around {guild.member_count} minutes", colour=discord.Color.blurple()))
            for member in guild.members:
                await member.add_roles(roles=role , reason=f"Added by {interaction.user.name}")
                await asyncio.sleep(60)
                if role in member:
                    continue
                await message.edit(embed=discord.Embed(description=f"**Status:** Adding role to {guild.member_count} added role to {member.mention}\nWill take around {guild.member_count} minutes", colour=discord.Color.blurple()))
            await message.edit(embed=discord.Embed(description="**Status:** Done!" , colour=discord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return
        
    @role_slash.command(name="other" , description="add a role to all the member in the guild")
    async def role_slash_other(self,interaction: discord.Interaction , role: discord.Role):
        try:
            guild = interaction.guild
            message = await interaction.response.send_message(embed=discord.Embed(description=f"**Status:** Adding role to {guild.member_count - 1} \nWill take around {guild.member_count - 1} minutes", colour=discord.Color.blurple()))
            for member in guild.members:
                await member.add_roles(roles=role , reason=f"Added by {interaction.user.name}")
                await asyncio.sleep(60)
                if role in member:
                    continue
                if member.id == interaction.user.id:
                    continue
                await message.edit(embed=discord.Embed(description=f"**Status:** Adding role to {guild.member_count - 1} added role to {member.mention}\nWill take around {guild.member_count - 1} minutes", colour=discord.Color.blurple()))
            await message.edit(embed=discord.Embed(description="**Status:** Done!" , colour=discord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return

    @role_slash.command(name="add" , description="add role to mentioned member")
    async def role_slash_add(self,interaction: discord.Interaction , member: discord.Member , role: discord.Role):
        try:
            if role in member:
                await interaction.response.send_message(f"{member.mention} already have {role.mention}" , ephemeral=True)
                return
            await member.add_roles(roles=role , reason=f"Added by {interaction.user.name}")
            await interaction.response.send_message(embed=discord.Embed(description=f"added role to {member.mention}", colour=discord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return
        
    @role_slash.command(name="remove" , description="add role to mentioned member")
    async def role_slash_remove(self,interaction: discord.Interaction , member: discord.Member , role: discord.Role):
        try:
            if not role in member:
                await interaction.response.send_message(f"{member.mention} doesn't have {role.mention}" , ephemeral=True)
                return
            await member.remove_roles(roles=role , reason=f"Removed by {interaction.user.name}")
            await interaction.response.send_message(embed=discord.Embed(description=f"Removed role from {member.mention}", colour=discord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return
        
    @commands.command("role")
    @commands.has_permissions(manage_roles=True)
    async def role_prefix(self,ctx:commands.Context , member:discord.Member , role: discord.Role):
        try:
            if role in member:
                await member.remove_roles(roles=role , reason=f"Removed by {ctx.author.name}")
                await ctx.reply(embed=discord.Embed(description=f"Status: removed role from {member.mention}", colour=discord.Color.blurple()).set_footer(text=f"command ran by {ctx.author.name}"))
            else:
                await member.add_roles(roles=role , reason=f"Removed by {ctx.author.name}")
                await ctx.reply(embed=discord.Embed(description=f"Status: added role to {member.mention}", colour=discord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await ctx.reply("role that you mentioned is higher or same level as bot please mention lower level role")
        else:
            return
    
async def setup(bot):
    await bot.add_cog(role(bot))