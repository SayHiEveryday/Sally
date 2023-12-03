import discord
from discord.ext import commands
from utils.arg import bot
from discord import app_commands
#banner is broken

class getprofile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def avatar(self,interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title=f"**Avatar of {member.name}**").set_image(member.avatar.url).set_footer(text=f"command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @commands.command(name="banner")
    async def banner_prefix(self,ctx: commands.Context, member: discord.Member):
        try:
            user = await bot.fetch_user(member.id)
            
            embed = discord.Embed(title=f"**Banner of {member.name}**").set_image(user.banner.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)
        except NameError:
            await ctx.reply("this person doesn't have banner")
        except Exception:
            await ctx.reply("this command is broken and will be fix later")


    @commands.command(name="avatar")
    async def avatar_prefix(self,ctx, member: discord.Member):
        embed = discord.Embed(title=f"**Avatar of {member.name}**").set_image(member.display_avatar.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @avatar_prefix.error
    async def avatar_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=f"**Avatar of {ctx.author.name}**").set_image(ctx.author.display_avatar.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)

    @banner_prefix.error
    async def banner_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            try:
                embed = discord.Embed(title=f"**Avatar of {ctx.author.name}**").set_image(ctx.author.display_avatar.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
                await ctx.send(embed=embed)
            except NameError:
                return


async def setup(bot):
    await bot.add_cog(getprofile(bot))