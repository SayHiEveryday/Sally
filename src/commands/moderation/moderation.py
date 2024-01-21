import discord
from discord.ext import commands
import datetime , humanfriendly
from discord import app_commands

class _moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    mod = app_commands.Group(name="moderation",description="Moderation module")


    @mod.command(name="kick" , description="Kick a member")
    @app_commands.default_permissions(kick_members=True)
    async def _kick(self,interaction: discord.Interaction , member: discord.Member , reason: str = "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't kick a member who has administrator permission" , ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't kick a bot D:" , ephemeral=True)
            return
        if member.id == interaction.user.id:
            await interaction.response.send_message("Hey! you can't kick yourself" , ephemeral=True)
            return
        
        await interaction.response.send_message("Success" , ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been kicked | {reason}",colour=0x3BA55C)
        await member.kick(reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        await interaction.channel.send(embed=embed)


    @mod.command(name="ban" , description="Ban a member")
    @app_commands.default_permissions(ban_members=True)
    async def _ban(self,interaction: discord.Interaction , member: discord.Member , reason: str = "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't ban a member who has administrator permission" , ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't ban a bot D:" , ephemeral=True)
            return
        if member.id == interaction.user.id:
            await interaction.response.send_message("Hey! you can't ban yourself" , ephemeral=True)
            return
        
        await interaction.response.send_message("Success" , ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been banned | {reason}",colour=0x3BA55C)
        await member.ban(reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        await interaction.channel.send(embed=embed)

    @mod.command(name="mute",description="timeout a member")
    @app_commands.default_permissions(moderate_members=True)
    @app_commands.describe(
        member="member to timeout",
        time="duration ( 1d 2m 3s )",
        reason="reason to timeout"
    )
    async def _mute(self,interaction:discord.Interaction,member:discord.Member,time:str,reason:str= "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't mute a member who has administrator permission",ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't mute a bot D:" , ephemeral=True)
            return
        if member == interaction.user:
            await interaction.response.send_message("Hey! you can't mute yourself" , ephemeral=True)
            return
        try:
            r = humanfriendly.parse_timespan(time)
        except:
            await interaction.response.send_message(f"Invalid time. Example: `1d` `2m`",ephemeral=True)
            return
        
        try:
            await member.timeout(discord.utils.utcnow() + datetime.timedelta(seconds=r),reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        except:
            await interaction.response.send_message(f"Failed to mute {member.mention}",ephemeral=True)
            return
        await interaction.response.send_message("success",ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been muted for {time} | {reason}",colour=0x3BA55C)
        await interaction.channel.send(embed=embed)

    @mod.command(name="unmute",description="remove timeout from a member")
    @app_commands.default_permissions(moderate_members=True)
    async def _unmute(self,interaction:discord.Interaction,member: discord.Member,reason:str= "Moderator didn't specific a reason"):
        if not member.is_timed_out():
            await interaction.response.send_message(f"{member.mention} isn't muted",ephemeral=True)
            return
        try:
            await member.timeout(None,reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        except:
            await interaction.response.send_message(f"Fail to unmute {member.mention}",ephemeral=True)
            return
        await interaction.response.send_message("success",ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been unmuted | {reason}",colour=0x3BA55C)
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
    await bot.add_cog(_moderation(bot))
