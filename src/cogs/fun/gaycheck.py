import nextcord
from nextcord.ext import commands
import random
import datetime
import asyncio

class gaycheck(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="gay" , description="feeling like someone is gay? Test them!")
    async def gaycheck_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        embed1 = nextcord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is {random.randint(1,100)}% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed2 = nextcord.Embed(title="**Gay test in process 1/2**",description=f"Looking at <@{member.id}>'s face",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed3 = nextcord.Embed(title="**Gay test in process 2/2**",description=f"Checking <@{member.id}>'s browser history",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        embed4 = nextcord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is 0% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)

        msg = await interaction.response.send_message(embed=embed2)
        await asyncio.sleep(random.randint(1,5))
        await msg.edit(embed=embed3)
        await asyncio.sleep(random.randint(1,5))
        if member.id == 698851209032761384:
            await msg.edit(embed=embed4)
        else:
            await msg.edit(embed=embed1)

    @commands.command(name="gay")
    async def gaycheck_prefix(self,ctx, member: nextcord.Member):
        embed1 = nextcord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is {random.randint(1,100)}% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed2 = nextcord.Embed(title="**Gay test in process 1/2**",description=f"Looking at <@{member.id}>'s face",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed3 = nextcord.Embed(title="**Gay test in process 2/2**",description=f"Checking <@{member.id}>'s browser history",colour=0xff0000,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed4 = nextcord.Embed(title="**Gay test successfully**",description=f"<@{member.id}> is 0% gay",colour=0x44ff00,timestamp=datetime.datetime.now()).set_footer(text=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url)
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

def setup(bot):
    bot.add_cog(gaycheck(bot))
