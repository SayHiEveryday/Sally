import discord
from discord.ext import commands
from utils.arg import bot
from discord import app_commands

class pingcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def pings(self,interaction: discord.Interaction):
        await interaction.send(f"Pong! my ping is `{round(bot.latency) * 1000}` ms , websocket is `{round(bot.ws.latency) * 1000}` ms")

    @commands.command()
    async def ping(self,interaction: discord.Interaction):
        await interaction.send(f"Pong! my ping is `{round(bot.latency) * 1000}` ms , websocket is `{round(bot.ws.latency) * 1000}` ms")


async def setup(bot):
    await bot.add_cog(pingcmd(bot))