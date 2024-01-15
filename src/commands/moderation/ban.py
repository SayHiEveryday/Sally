import discord
from discord.ext import commands
import datetime
from utils.handler.getprefix import get_prefix
from discord import app_commands

class ban(commands.Cog):
    def __init__(self,client):
        self.client = client

    @app_commands.command(name="ban" , description="Ban a member")
    @app_commands.default_permissions(ban_members=True)
    async def ban_slash(self,interaction: discord.Interaction , member: discord.Member , reason: str = "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't ban a member who have administrator permission" , ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't ban a bot D:" , ephemeral=True)
            return
        if member.id == interaction.user.id:
            await interaction.response.send_message("Hey! you can't ban yourself" , ephemeral=True)

        await interaction.response.send_message("Success" , ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been banned | {reason}",colour=0x3BA55C)
        await member.ban(reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        await interaction.channel.send(embed=embed)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban_prefix(self,ctx, member: discord.Member ,*, reason:str="Moderator didn't specific a reason"):
        if member == None:
            await ctx.reply("You need to mention a member to ban!")
            return
        if member.guild_permissions.administrator:
            await ctx.reply("I can't ban a member who have administrator permission")
            return
        if member.bot.real:
            await ctx.send("i can't ban a bot D:")
            return
        
        if member.id == ctx.author.id:
            await ctx.send("Hey! you can't ban yourself")
            return
        
        await ctx.message.delete()
        embed = discord.Embed(description=f"{member.name} has been banned | {reason}",colour=0x3BA55C)
        await member.ban(reason=f"Moderator: {ctx.author.name} , Reason: {reason}")
        await ctx.channel.send(embed=embed)

    @ban_prefix.error
    async def on_error(self,ctx , error):
        if isinstance(error , commands.MissingPermissions):
            await ctx.reply("Missing Permission: `ban_members`")
            return
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.reply(error)


async def setup(bot):
    await bot.add_cog(ban(bot))