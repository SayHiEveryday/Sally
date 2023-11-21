import nextcord
from nextcord.ext import commands


class getprofile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="get_profile" , description="Get someone's profile")
    async def profile_slash(self,interaction: nextcord.Interaction , member: nextcord.Member , ty = nextcord.SlashOption(name="type" , choices=["banner" , "profile_picture"])):
        if ty == "banner":
            if not member.banner == None:
                ty2 = member.banner.url
            else:
                await interaction.response.send_message("This person doesn't have banner")
        else:
            ty2 = member.display_avatar.url

        embed = nextcord.Embed(title=f"**{ty} of {member.name}**").set_image(ty2).set_footer(text=f"command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @commands.command(name="banner")
    async def banner_prefix(self,ctx: commands.Context, member: nextcord.Member):
        try:
            embed = nextcord.Embed(title=f"**Banner of {member.name}**").set_image(member.banner.url).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)
        except NameError:
            await ctx.reply("this person doesn't have banner")

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