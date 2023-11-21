import nextcord
from nextcord.ext import commands
from utils.api import ram


class slap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="slap" , description="dislike someone? slap them!")
    async def slap_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> slap themself hope {interaction.user.name} is okay D:")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> slap robot but robot doesn't have feeling.")
            return

        await interaction.response.defer()
        embed = nextcord.Embed(title=f"**{interaction.user.name} slap {member.name}! , Hope {member.name} is okay D:**").set_image(ram.rammore("slap"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="slap")
    async def slap_prefix(self,ctx, member: nextcord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> slap themself hope {ctx.author.name} is okay D:")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> slap robot but robot doesn't have feeling.")
            return

        embed = nextcord.Embed(title=f"**{ctx.author.name} slap {member.name}! , Hope {member.name} is okay D:**").set_image(ram.rammore("slap"))
        await ctx.send(embed=embed)

    @slap_prefix.error
    async def slap_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't slap air")

def setup(bot):
    bot.add_cog(slap(bot))