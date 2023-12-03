import discord
from utils.api.urban import urban
from discord.ext import commands
from discord import app_commands

class urban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="urban" , description="Search urban dictionary")
    async def urban_slash(self,interaction: discord.Interaction , word:str):
        get = urban(word)
        embed = discord.Embed(title=f"**Result for {word}**" , description=f"**definition:** {get['Definition']}\n**Link:** {get['permalink']}\n**Author:** {get['author']}\n**Written on:** {get['written_on']}\n**Example:** {get['example']}" , colour=0x5865F2)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(urban(bot))