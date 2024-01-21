import discord , datetime
from discord.ext import commands
import pykitsu
from discord import app_commands

class _kitsu(commands.Cog):
    def __init__(self, client):
        self.client = client

    kitsu = app_commands.Group(name="kitsu",description="Search anime from kitsu.io")

    @kitsu.command(name="search",description="Search anime/manga from kitsu.io")
    @app_commands.choices(type=[
        app_commands.Choice(name="anime",value="anime"),
        app_commands.Choice(name="manga",value="manga")
    ])
    async def _search(self,interaction:discord.Interaction,type:app_commands.Choice[str],name:str):
        await interaction.response.defer()
        client = pykitsu.Client()
        while 5 > 2:
            anime = client.search(search_term=name, type=type.value, debug_outputs=False, limit_requests=True)
            try:
                n = await anime.name()
                plot = await anime.plot()
                airing_start_date = await anime.airing_start_date()
                airing_end_date = await anime.airing_end_date()
                nsfw_status = await anime.nsfw_status()
                p = await anime.poster_url()
                embed = discord.Embed(title=f"Search result for {name}",colour=discord.Color.random())
                embed.add_field(name="name",value=n,inline=False)
                embed.add_field(name="plot",value=plot,inline=False)
                embed.add_field(name="airing start date",value=airing_start_date,inline=True)
                embed.add_field(name="airing end date",value=airing_end_date,inline=True)
                embed.add_field(name="is nsfw?",value=nsfw_status,inline=False)
                embed.set_image(url=p)
                await anime.clear_cache()
                break
            except pykitsu.NO_DATA_FOUND:
                await interaction.followup.send(f"No result found for {name}")
                return
            
        await interaction.followup.send(embed=embed)

    @kitsu.command(name="random",description="Return random anime")
    async def _random(self,interaction:discord.Interaction):
        t = "anime"
        await interaction.response.defer()
        client = pykitsu.Client()
        while 5 > 2:
            anime = client.random(type=t, debug_outputs=False, limit_requests=True)
        
            try:
                
                n = await anime.name()
                plot = await anime.plot()
                airing_start_date = await anime.airing_start_date()
                airing_end_date = await anime.airing_end_date()
                nsfw_status = await anime.nsfw_status()
                p = await anime.poster_url()
                embed = discord.Embed(title=f"Result {n}",colour=discord.Color.random())
                embed.add_field(name="name",value=n,inline=False)
                embed.add_field(name="plot",value=plot,inline=False)
                embed.add_field(name="airing start date",value=airing_start_date,inline=True)
                embed.add_field(name="airing end date",value=airing_end_date,inline=True)
                embed.add_field(name="is nsfw?",value=nsfw_status,inline=False)
                embed.set_image(url=p)
                break
            except pykitsu.NO_DATA_FOUND:
                await interaction.followup.send("something error")
                return
        await interaction.followup.send(embed=embed)


async def setup(bot):
    await bot.add_cog(_kitsu(bot))    
        
