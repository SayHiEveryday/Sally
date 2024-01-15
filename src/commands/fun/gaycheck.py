import discord
from discord.ext import commands
import random
import datetime
import asyncio
from discord import app_commands

class gaycheck(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @app_commands.command(name="gay" , description="feeling like someone is gay? Test them!")
    async def gaycheck_slash(self,interaction: discord.Interaction , member: discord.Member):
        embed1 = discord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is {random.randint(1,100)}% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed2 = discord.Embed(title="**Gay test in process 1/2**",description=f"Looking at <@{member.id}>'s face",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed3 = discord.Embed(title="**Gay test in process 2/2**",description=f"Checking <@{member.id}>'s browser history",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed4 = discord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is 0% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)

        await interaction.response.send_message(embed=embed2)
        msg = await interaction.original_response()
        await asyncio.sleep(random.randint(1,5))
        await msg.edit(embed=embed3)
        await asyncio.sleep(random.randint(1,5))
        if member.id == 698851209032761384:
            await msg.edit(embed=embed4)
        else:
            await msg.edit(embed=embed1)

    @commands.command(name="gay")
    async def gaycheck_prefix(self,ctx:commands.Context, member: discord.Member):
        embed1 = discord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is {random.randint(1,100)}% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed2 = discord.Embed(title="**Gay test in process 1/2**",description=f"Looking at <@{member.id}>'s face",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed3 = discord.Embed(title="**Gay test in process 2/2**",description=f"Checking <@{member.id}>'s browser history",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed4 = discord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is 0% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        msg = await ctx.send(embed=embed2)
        await asyncio.sleep(random.randint(1,5))
        await msg.edit(embed=embed3)
        await asyncio.sleep(random.randint(1,5))
        if member.id == 698851209032761384:
            await msg.edit(embed=embed4)
        else:
            await msg.edit(embed=embed1)
        
    @gaycheck_prefix.error
    async def gaycheck_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't gay test an air!")

async def setup(bot):
    await bot.add_cog(gaycheck(bot))
