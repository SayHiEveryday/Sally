import discord
from discord.ext import commands
import aiosqlite
from discord import app_commands

class _settings(commands.Cog):
    def __init__(self, client):
        self.client = client

    settings = app_commands.Group(name="settings",description="Settings")

    @settings.command(description="Allow nsfw commands?")
    @app_commands.default_permissions(administrator=True)
    async def nsfw(self,interaction:discord.Interaction,allow:bool):
        await interaction.response.defer(ephemeral=True)
        if not interaction.user.guild_permissions.administrator:
            await interaction.followup.send("You are not allow to execute this commands. Required `administrator`")
            return
        
        match allow:
            case True:
                allowed = "1"
            case False:
                allowed = "0"
        
        async with aiosqlite.connect("storage/settings.sqlite") as db:
            await db.execute(f"UPDATE perguild SET nsfw = '{allowed}' WHERE guild = '{interaction.guild.id}'")
            await db.commit()
        await interaction.followup.send("Successfully updated settings")

    @settings.command(name="prefix" , description="Change bot prefix")
    @app_commands.default_permissions(administrator=True)
    async def changeprefix_slash(self,interaction: discord.Interaction , newprefix:str):
        
        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            await db.execute(f"UPDATE prefix SET prefix = '{str(newprefix)}' WHERE guild = {interaction.guild.id}")
            await db.commit()

        await interaction.response.send_message(f"Prefix changed! new prefix: {newprefix}")

    @commands.command(name="change_prefix")
    @commands.has_permissions(administrator=True)
    async def changeprefix_prefix(self,ctx , newprefix:str):
        
        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            await db.execute(f"UPDATE prefix SET prefix = '{str(newprefix)}' WHERE guild = {ctx.guild.id}")
            await db.commit()

        await ctx.reply(f"Prefix changed! new prefix: {newprefix}")


    @changeprefix_prefix.error
    async def error(self,ctx,error):
        pass

async def setup(bot):
    await bot.add_cog(_settings(bot))