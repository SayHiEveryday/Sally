import discord 
from utils.api import ram
from discord.ext import commands
from discord import app_commands

class pout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="pout" , description="Send pout gif")
    async def pout_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            embed = discord.Embed(
                title=f"{interaction.user.name} pouts themself",
                colour=discord.Color.random(),
            ).set_image(
                url=ram.rammore("pout")
            ).set_footer(
                text="command ran by {}".format(interaction.user.name),
                icon_url=interaction.user.display_avatar.url
            )
            await interaction.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            title=f"{interaction.user.name} pouts at {member.name}",
            colour=discord.Color.random()
        ).set_footer(
            text="command ran by {}".format(interaction.user.name),
            icon_url=interaction.user.display_avatar.url
        ).set_image(
            ram.rammore("pout")
        )
        await interaction.response.send_message(embed=embed)

    @commands.command(name="pout")
    async def pout_prefix(self,ctx,member:discord.Member):
        embed = discord.Embed(
            title=f"{ctx.author.name} pouts at {member.name}",
            colour=discord.Color.random()
        ).set_footer(
            text="command ran by {}".format(ctx.author.name),
            icon_url=ctx.author.display_avatar.url
        ).set_image(
            url=ram.rammore("pout")
        )
        await ctx.send(embed=embed)

    @pout_prefix.error
    async def pout_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title=f"{ctx.authot.name} pouts themself",
                colour=discord.Color.random(),
            ).set_image(
                url=ram.rammore("pout")
            ).set_footer(
                text="command ran by {}".format(ctx.author.name),
                icon_url=ctx.author.display_avatar.url
            )
            await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(pout(bot))