import discord
from discord.ext import commands
from utils.api import ram
from discord import app_commands

class cuddle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="cuddle" , description="like someone? cuddle them!")
    async def cuddle_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"Okay, <@{interaction.user.id}> cuddle themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"Okay seem like <@{interaction.user.id}> in love with robot")
            return
        
        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} cuddle {member.name}!**").set_image(ram.rammore("cuddle"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="cuddle")
    async def cuddle_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"Okay, <@{ctx.author.id}> cuddle themself")
            return
        if member.bot.real:
            await ctx.send(f"Okay seem like <@{ctx.author.id}> in love with robot")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} cuddle {member.name}!**").set_image(ram.rammore("cuddle"))
        await ctx.send(embed=embed)
        
    @cuddle_prefix.error
    async def cuddle_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't cuddle air")

async def setup(bot):
    await bot.add_cog(cuddle(bot))