import nextcord
from nextcord.ext import commands
from utils.api import ram

class kiss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="kiss" , description="Have feeling with someone? kiss them!")
    async def kiss_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> kiss themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> kiss robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = nextcord.Embed(title=f"**{interaction.user.name} kiss {member.name}!**").set_image(ram.rammore("kiss"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="kiss")
    async def kiss_prefix(self,ctx, member: nextcord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> kiss themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> kiss robot but robot doesn't have feeling.")
            return

        embed = nextcord.Embed(title=f"**{ctx.author.name} kiss {member.name}!**").set_image(ram.rammore("kiss"))
        await ctx.send(embed=embed)

    @kiss_prefix.error
    async def kiss_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't kiss air")

def setup(bot):
    bot.add_cog(kiss(bot))