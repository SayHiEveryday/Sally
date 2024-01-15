import discord , requests , time
from discord.ext import commands
from discord import app_commands

class nekoapi(commands.Cog):
    def __init__(self, client):
        self.client = client

    image = app_commands.Group(name="imagegen",description="generate image using nekobot.xyz api")

    @image.command(name="change_my_mine",description="Generate image about change my mind")
    async def image_cmm(self,interaction: discord.Interaction,text:str):
        await interaction.response.defer()
        start = time.time()
        res = text.replace(" ","%20")
        re = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={res}")
        embed = discord.Embed(colour=discord.Color.random())
        embed.set_image(url=re.json()['message'])
        embed.set_footer(text=f"Execution took {round(time.time() - start)} seconds")
        await interaction.followup.send(embed=embed)

    @image.command(name="who_would_win",description="who would win")
    @app_commands.describe(member="Member that you want to fight with")
    async def image_www(self,interaction: discord.Interaction,member:discord.Member):
        start = time.time()
        await interaction.response.defer()
        re = requests.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={interaction.user.display_avatar.url}&user2={member.display_avatar.url}")
        embed = discord.Embed(colour=discord.Color.random())
        embed.set_image(url=re.json()['message'])
        embed.set_footer(text=f"Execution took {round(time.time() - start)} seconds")
        await interaction.followup.send(embed=embed)

    @image.command(name="kannagen",description="Generate kanna holding paper with inputed text")
    @app_commands.describe(text="text you want kanna to hold")
    async def image_kg(self,interaction: discord.Interaction,text:str):
        await interaction.response.defer()
        start = time.time()
        res = text.replace(" ","%20")
        re = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={res}")
        embed = discord.Embed(colour=discord.Color.random())
        embed.set_image(url=re.json()['message'])
        embed.set_footer(text=f"Execution took {round(time.time() - start)} seconds")
        await interaction.followup.send(embed=embed)
    @image.command(name="trapcard",description="Make mentioned member stuck in trapcard")
    @app_commands.describe(member="member you want to trap")
    async def image_trap(self,interaction: discord.Interaction,member:discord.Member):
        await interaction.response.defer()
        start = time.time()
        re = requests.get(f"https://nekobot.xyz/api/imagegen?type=trap&image={member.display_avatar.url}&name={member.display_name}&author={interaction.user.display_name}")
        embed = discord.Embed(colour=discord.Color.random())
        embed.set_image(url=re.json()['message'])
        embed.set_footer(text=f"Execution took {round(time.time() - start)} seconds")
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(nekoapi(bot))