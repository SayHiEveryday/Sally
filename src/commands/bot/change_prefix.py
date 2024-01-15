import discord , json , os , aiosqlite
from discord.ext import commands
from discord import app_commands
from utils.handler.logcmd import *

class change_prefix(commands.Cog):
    def __init__(self, client):
        self.client = client
    @app_commands.command(name="change_prefix" , description="Change bot prefix")
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
        if isinstance(error , commands.MissingRequiredArgument):
            
            with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
                prefix = json.load(f)

            await ctx.reply(f"Hey what prefix are you going to change to , Your current prefix is **{prefix[str(ctx.guild.id)]}**")


async def setup(bot):
    await bot.add_cog(change_prefix(bot))