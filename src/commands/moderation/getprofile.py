import nextcord
from nextcord.ext import commands
from utils.arg import bot

#banner is broken

class getprofile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="get_profile" , description="Get someone's profile")
    async def profile_slash(self,interaction: nextcord.Interaction , member: nextcord.Member , ty = nextcord.SlashOption(name="type" , choices=["banner" , "profile_picture"])):
        try:
            if ty == "banner":
                user = await bot.fetch_user(member.id)
                ty2 = user.banner.url
            else:
                ty2 = member.display_avatar.url

            embed = nextcord.Embed(title=f"**{ty} of {member.name}**").set_image(ty2).set_footer(text=f"command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=embed)
        except Exception:
            await interaction.response.send_message("this command is broken will be fix later" , ephemeral=True)

    @commands.command(name="banner")
    async def banner_prefix(self,ctx: commands.Context, member: nextcord.Member):
        try:
            user = await bot.fetch_user(member.id)
            
            embed = nextcord.Embed(title=f"**Banner of {member.name}**").set_image(user.banner.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)
        except NameError:
            await ctx.reply("this person doesn't have banner")
        except Exception:
            await ctx.reply("this command is broken and will be fix later")


    @commands.command(name="avatar")
    async def avatar_prefix(self,ctx, member: nextcord.Member):
        embed = nextcord.Embed(title=f"**Avatar of {member.name}**").set_image(member.display_avatar.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @avatar_prefix.error
    async def avatar_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(title=f"**Avatar of {ctx.author.name}**").set_image(ctx.author.display_avatar.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)

    @banner_prefix.error
    async def banner_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            try:
                embed = nextcord.Embed(title=f"**Avatar of {ctx.author.name}**").set_image(ctx.author.display_avatar.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
                await ctx.send(embed=embed)
            except NameError:
                return


def setup(bot):
    bot.add_cog(getprofile(bot))