import nextcord
from nextcord.ext import commands
from utils.api.ram import rammore

class hug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="hug" , description="Someone being cute? hug them!")
    async def hug_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> hug themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> hug robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = nextcord.Embed(title=f"**{interaction.user.name} hug {member.name}!**").set_image(rammore("hug"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="hug")
    async def hug_prefix(self,ctx, member: nextcord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> hug themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> hug robot but robot doesn't have feeling.")
            return

        embed = nextcord.Embed(title=f"**{ctx.author.name} hug {member.name}!**").set_image(rammore("hug"))
        await ctx.send(embed=embed)

    @hug_prefix.error
    async def hug_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't hug air")


def setup(bot):
    bot.add_cog(hug(bot))