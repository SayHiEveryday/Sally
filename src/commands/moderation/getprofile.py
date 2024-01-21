import discord
from discord.ext import commands
from storage.arg import bot
from discord import app_commands

class getprofile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(description="get mentioned user's avatar")
    async def avatar(self,interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title=f"**Avatar of {member.name}**").set_image(url=member.avatar.url) 
        await interaction.response.send_message(embed=embed)
    
    @commands.command(name="avatar",aliases=['av','profile'])
    async def avatar_prefix(self,ctx, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(title=f"**Avatar of {ctx.author}**").set_image(url=ctx.author.display_avatar.url) 
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title=f"**Avatar of {member.name}**").set_image(url=member.display_avatar.url) 
        await ctx.send(embed=embed)

    @avatar_prefix.error
    async def avatar_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=f"**Avatar of {ctx.author.name}**").set_image(url=ctx.author.display_avatar.url) 
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(getprofile(bot))
