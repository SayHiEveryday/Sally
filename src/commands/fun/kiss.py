import discord
from discord.ext import commands
from utils.api import ram
from discord import app_commands

class kiss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="kiss" , description="Have feeling with someone? kiss them!")
    async def kiss_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> kiss themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> kiss robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} kiss {member.name}!**").set_image(ram.rammore("kiss"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="kiss")
    async def kiss_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> kiss themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> kiss robot but robot doesn't have feeling.")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} kiss {member.name}!**").set_image(ram.rammore("kiss"))
        await ctx.send(embed=embed)

    @kiss_prefix.error
    async def kiss_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't kiss air")

async def setup(bot):
    await bot.add_cog(kiss(bot))