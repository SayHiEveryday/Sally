import discord
from discord.ext import commands
from utils.api import ram
from discord import app_commands

class slap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="slap" , description="dislike someone? slap them!")
    async def slap_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> slap themself hope {interaction.user.name} is okay D:")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> slap robot but robot doesn't have feeling.")
            return

        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} slap {member.name}! , Hope {member.name} is okay D:**").set_image(ram.rammore("slap"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="slap")
    async def slap_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> slap themself hope {ctx.author.name} is okay D:")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> slap robot but robot doesn't have feeling.")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} slap {member.name}! , Hope {member.name} is okay D:**").set_image(ram.rammore("slap"))
        await ctx.send(embed=embed)

    @slap_prefix.error
    async def slap_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't slap air")

async def setup(bot):
    await bot.add_cog(slap(bot))