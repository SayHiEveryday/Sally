import nextcord
from nextcord.ext import commands
from utils import api

class pat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="pat" , description="Someone being cute? pat them!")
    async def pat_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> pat themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> pat robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = nextcord.Embed(title=f"**{interaction.user.name} pat {member.name}!**").set_image(api.rammore("pat"))
        await interaction.followup.send(embed=embed)

    @commands.command(name="pat")
    async def pat_prefix(self,ctx, member: nextcord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> pat themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> pat robot but robot doesn't have feeling.")
            return

        embed = nextcord.Embed(title=f"**{ctx.author.name} pat {member.name}!**").set_image(api.rammore("pat"))
        await ctx.send(embed=embed)

    @pat_prefix.error
    async def pat_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't pat air")
    
def setup(bot):
    bot.add_cog(pat(bot))