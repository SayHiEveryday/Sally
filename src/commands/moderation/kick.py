import discord
from discord.ext import commands
import datetime
from utils.handler.getprefix import get_prefix
from discord import app_commands

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="kick" , description="Kick a member")
    @app_commands.default_permissions(kick_members=True)
    async def kick_slash(self,interaction: discord.Interaction , member: discord.Member , reason: str = "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't kick a member who have administrator permission" , ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't kick a bot D:" , ephemeral=True)
            return
        if member.id == interaction.user.id:
            await interaction.response.send_message("Hey! you can't kick yourself" , ephemeral=True)

        await interaction.response.send_message("Success" , ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been kicked | {reason}",colour=0x3BA55C)
        await member.kick(reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        await interaction.channel.send(embed=embed)

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_prefix(self,ctx, member: discord.Member ,*, reason: str = "Moderator didn't specific a reason"):
        if member == None:
            await ctx.reply("You need to mention a member to kick")
            return
        if member.guild_permissions.administrator:
            await ctx.reply("I can't kick a member who have administrator permission")
            return
        if member.bot.real:
            await ctx.send("i can't kick a bot D:")
            return
        
        if member.id == ctx.author.id:
            await ctx.send("Hey! you can't kick yourself")
            return
        
        await ctx.message.delete()
        embed = discord.Embed(description=f"{member.name} has been kicked | {reason}",colour=0x3BA55C)
        await member.kick(reason=f"Moderator: {ctx.author.name} , Reason: {reason}")
        await ctx.channel.send(embed=embed)

    @kick_prefix.error
    async def on_error(self,ctx , error):
        if isinstance(error , commands.MissingPermissions):
            await ctx.reply("Missing Permission: `kick_members`")
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.reply(error)

async def setup(bot):
    await bot.add_cog(kick(bot))