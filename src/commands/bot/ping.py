import discord
from discord.ext import commands
from storage.arg import bot
from discord import app_commands

class pingcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ping",description="Show latency between bot and discord gateway")
    async def ping_slash(self,interaction: discord.Interaction):
        shard_id = interaction.guild.shard_id
        shard = bot.get_shard(shard_id)
        await interaction.response.send_message(f"Pong! Shard ID for this server is {str(shard_id)} and My ping is `{round(shard.latency * 1000)}` ms")

    @commands.command()
    async def ping(self,ctx:commands.Context):
        shard_id = ctx.guild.shard_id
        shard = bot.get_shard(shard_id)
        await ctx.reply(f"Pong! Shard ID for this server is {str(shard_id)} and My ping is `{round(shard.latency * 1000)}` ms",mention_author=False)
async def setup(bot):
    await bot.add_cog(pingcmd(bot))
