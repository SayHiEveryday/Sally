import nextcord
from utils import api
from nextcord.ext import commands

class urban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="urban" , description="Search urban dictionary")
    async def urban_slash(self,interaction: nextcord.Interaction , word:str):
        get = api.urban(word)
        embed = nextcord.Embed(title=f"**Result for {word}**" , description=f"**definition:** {get['Definition']}\n**Link:** {get['permalink']}\n**Author:** {get['author']}\n**Written on:** {get['written_on']}\n**Example:** {get['example']}" , colour=0x5865F2)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(urban(bot))