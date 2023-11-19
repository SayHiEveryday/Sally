import nextcord
from nextcord.ext import commands
from utils.run import bot


class pingcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command()
    async def pings(self,interaction: nextcord.Interaction):
        await interaction.send(f"Pong! my ping is `{round(bot.latency)}` ms , websocket is `{round(bot.ws.latency)}` ms")

    @commands.command()
    async def ping(self,interaction: nextcord.Interaction):
        await interaction.send(f"Pong! my ping is `{round(bot.latency)}` ms , websocket is `{round(bot.ws.latency)}` ms")


def setup(bot):
    bot.add_cog(pingcmd(bot))