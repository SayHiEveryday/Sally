import nextcord 
from utils.api import ram
from nextcord.ext import commands

class pout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="pout" , description="Send pout gif")
    async def pout_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            embed = nextcord.Embed(
                title=f"{interaction.user.name} pouts themself",
                colour=nextcord.Color.random(),
            ).set_image(
                ram.rammore("pout")
            ).set_footer(
                text="command ran by {}".format(interaction.user.name),
                icon_url=interaction.user.display_avatar.url
            )
            await interaction.response.send_message(embed=embed)
            return
        embed = nextcord.Embed(
            title=f"{interaction.user.name} pouts at {member.name}",
            colour=nextcord.Color.random()
        ).set_footer(
            text="command ran by {}".format(interaction.user.name),
            icon_url=interaction.user.display_avatar.url
        ).set_image(
            ram.rammore("pout")
        )
        await interaction.response.send_message(embed=embed)

    @commands.command(name="pout")
    async def pout_prefix(self,ctx,member:nextcord.Member):
        embed = nextcord.Embed(
            title=f"{ctx.author.name} pouts at {member.name}",
            colour=nextcord.Color.random()
        ).set_footer(
            text="command ran by {}".format(ctx.author.name),
            icon_url=ctx.author.display_avatar.url
        ).set_image(
            ram.rammore("pout")
        )
        await ctx.send(embed=embed)

    @pout_prefix.error
    async def pout_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title=f"{ctx.authot.name} pouts themself",
                colour=nextcord.Color.random(),
            ).set_image(
                ram.rammore("pout")
            ).set_footer(
                text="command ran by {}".format(ctx.author.name),
                icon_url=ctx.author.display_avatar.url
            )
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(pout(bot))