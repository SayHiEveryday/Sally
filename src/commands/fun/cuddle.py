import nextcord
from nextcord.ext import commands
from utils.api import ram

class cuddle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="cuddle" , description="like someone? cuddle them!")
    async def cuddle_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"Okay, <@{interaction.user.id}> cuddle themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"Okay seem like <@{interaction.user.id}> in love with robot")
            return
        
        await interaction.response.defer()
        embed = nextcord.Embed(title=f"**{interaction.user.name} cuddle {member.name}!**").set_image(ram.rammore("cuddle"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="cuddle")
    async def cuddle_prefix(self,ctx, member: nextcord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"Okay, <@{ctx.author.id}> cuddle themself")
            return
        if member.bot.real:
            await ctx.send(f"Okay seem like <@{ctx.author.id}> in love with robot")
            return

        embed = nextcord.Embed(title=f"**{ctx.author.name} cuddle {member.name}!**").set_image(ram.rammore("cuddle"))
        await ctx.send(embed=embed)
        
    @cuddle_prefix.error
    async def cuddle_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't cuddle air")

def setup(bot):
    bot.add_cog(cuddle(bot))