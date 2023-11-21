import nextcord
from nextcord.ext import commands
import asyncio

class role(commands.Cog):
    def __init__(self, client):
        self.client = client


    @nextcord.slash_command(name="role-all" , description="add a role to all the member in the guild" , default_member_permissions=268435456)
    async def role_slash_all(interaction: nextcord.Interaction , role: nextcord.Role):
        try:
            guild = interaction.guild
            message = await interaction.response.send_message(embed=nextcord.Embed(description=f"**Status:** adding role to {guild.member_count} Will take around {guild.member_count} minutes", colour=nextcord.Color.blurple()))
            for member in guild.members:
                await member.add_roles(roles=role , reason=f"Added by {interaction.user.name}")
                await asyncio.sleep(60)
                if role in member:
                    continue
                await message.edit(embed=nextcord.Embed(description=f"**Status:** Adding role to {guild.member_count} added role to {member.mention}\nWill take around {guild.member_count} minutes", colour=nextcord.Color.blurple()))
            await message.edit(embed=nextcord.Embed(description="**Status:** Done!" , colour=nextcord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return
        
    @nextcord.slash_command(name="role-other" , description="add a role to all the member in the guild" , default_member_permissions=268435456)
    async def role_slash_other(interaction: nextcord.Interaction , role: nextcord.Role):
        try:
            guild = interaction.guild
            message = await interaction.response.send_message(embed=nextcord.Embed(description=f"**Status:** Adding role to {guild.member_count - 1} \nWill take around {guild.member_count - 1} minutes", colour=nextcord.Color.blurple()))
            for member in guild.members:
                await member.add_roles(roles=role , reason=f"Added by {interaction.user.name}")
                await asyncio.sleep(60)
                if role in member:
                    continue
                if member.id == interaction.user.id:
                    continue
                await message.edit(embed=nextcord.Embed(description=f"**Status:** Adding role to {guild.member_count - 1} added role to {member.mention}\nWill take around {guild.member_count - 1} minutes", colour=nextcord.Color.blurple()))
            await message.edit(embed=nextcord.Embed(description="**Status:** Done!" , colour=nextcord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return

    @nextcord.slsah_command(name="role-add" , description="add role to mentioned member" , default_member_permissions=268435456)
    async def role_slash_add(interaction: nextcord.Interaction , member: nextcord.Member , role: nextcord.Role):
        try:
            if role in member:
                await interaction.response.send_message(f"{member.mention} already have {role.mention}" , ephemeral=True)
                return
            await member.add_roles(roles=role , reason=f"Added by {interaction.user.name}")
            await interaction.response.send_message(embed=nextcord.Embed(description=f"added role to {member.mention}", colour=nextcord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return
        
    @nextcord.slash_command(name="role-remove" , description="remove role to mentioned member" , default_member_permissions=268435456)
    async def role_slash_remove(interaction: nextcord.Interaction , member: nextcord.Member , role: nextcord.Role):
        try:
            if not role in member:
                await interaction.response.send_message(f"{member.mention} doesn't have {role.mention}" , ephemeral=True)
                return
            await member.remove_roles(roles=role , reason=f"Removed by {interaction.user.name}")
            await interaction.response.send_message(embed=nextcord.Embed(description=f"Removed role from {member.mention}", colour=nextcord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("role that you mentioned is higher or same level as bot please mention lower level role" , ephemeral=True)
        else:
            return
        
    @commands.command("role")
    @commands.has_permissions(manage_roles=True)
    async def role_prefix(ctx:commands.Context , member:nextcord.Member , role: nextcord.Role):
        try:
            if role in member:
                await member.remove_roles(roles=role , reason=f"Removed by {ctx.author.name}")
                await ctx.reply(embed=nextcord.Embed(description=f"Status: removed role from {member.mention}", colour=nextcord.Color.blurple()).set_footer(text=f"command ran by {ctx.author.name}"))
            else:
                await member.add_roles(roles=role , reason=f"Removed by {ctx.author.name}")
                await ctx.reply(embed=nextcord.Embed(description=f"Status: added role to {member.mention}", colour=nextcord.Color.blurple()))
        except Exception as e:
            if "403" in str(e):
                await ctx.reply("role that you mentioned is higher or same level as bot please mention lower level role")
        else:
            return
    
def setup(bot):
    bot.addcog(role(bot))