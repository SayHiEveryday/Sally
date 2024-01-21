import discord 
from discord.ext import commands
from storage.arg import bot
class on_mem_join(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_member_join(self,member: discord.Member):
        if member.guild.id == 1170654484905599016:
            role = discord.utils.get(member.guild.roles, id=1171020063420190771)
            await member.add_roles(role,reason="guild join")

async def setup(bot):
    await bot.add_cog(on_mem_join(bot))

