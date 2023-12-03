import discord
import discord.ext 
from discord.ext import commands
import asyncio
import random
import datetime
from discord import app_commands

class stealnitro(commands.Cog):
    def __init__(self, client):
        self.client = client
    @app_commands.command(name="stealnitro" , description="being poor? just steal other people nitro!")
    async def steals(self,interaction: discord.Interaction , member: discord.Member):
        if member.bot.real:
            await interaction.send("you can't steal bot nitro :skull: :skull: :skull: :skull:")
            return
        
        if member.id == interaction.user.id:
            await interaction.send("you can't steal your own nitro :skull: :skull: :skull: :skull:")
            return

        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(description="```checking user 1/3```")
            embed2 = discord.Embed(description="```stealing nitro 2/3 \n```")
            embed3 = discord.Embed(description=f"```sending nitro to {interaction.user.name} 3/3```")
            await interaction.send(embed=embed)
            await asyncio.sleep(random.randint(1,3))
            await interaction.edit_original_message(embed=embed2)
            await asyncio.sleep(random.randint(1,3))
            take = random.randint(1,4)
            if take == 1:
                await asyncio.sleep(random.randint(1,3))
                await interaction.edit_original_message(embed=embed3)
                await asyncio.sleep(random.randint(1,3))
                embed1 = discord.Embed(title="**Success**" , description=f"{interaction.user.mention} have successfully steal nitro from <@{member.id}> \n **your nitro will last for {random.randint(1,60)} minutes**")
                embed1.set_footer(icon_url=interaction.user.display_avatar.url , text=f"Commands ran by {interaction.user.name}")
                await interaction.edit_original_message(embed=embed1)
            else:
                embed4 = discord.Embed(title="Failed :sob:" , description=f"Fail to steal nitro from {member.mention}")
                embed4.set_footer(icon_url=interaction.user.display_avatar.url , text=f"Commands ran by {interaction.user.name}")
                await interaction.edit_original_message(embed=embed4)
                take2 = random.randint(1,2)
                if take2 == 1:
                    await asyncio.sleep(1)
                    embed5 = discord.Embed(title="Failed :sob:" , description=f"Fail to steal nitro from {member.mention} \n but instead {member.mention} steal {interaction.user.mention}'s nitro \n **and the nitro will last for {random.randint(1,60)} minutes**")
                    embed5.set_footer(icon_url=interaction.user.display_avatar.url , text=f"Commands ran by {interaction.user.name}")
                    await interaction.edit_original_message(embed=embed5)
                    
    @commands.command(name="stealnitro")
    async def stealp(self,ctx, member: discord.Member):
        if member.bot.real:
            await ctx.send("you can't steal bot nitro :skull: :skull: :skull: :skull:")
            return
        
        if member.id == ctx.author.id:
            await ctx.send("you can't steal your own nitro :skull: :skull: :skull: :skull:")
            return

        
        embed = discord.Embed(description="```checking user 1/3```")
        embed2 = discord.Embed(description="```stealing nitro 2/3 \n```")
        embed3 = discord.Embed(description=f"```sending nitro to {ctx.author.name} 3/3```")
        message = await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(1,3))
        await message.edit(embed=embed2)
        await asyncio.sleep(random.randint(1,3))
        take = random.randint(1,4)
        if take == 1:
            await asyncio.sleep(random.randint(1,3))
            await message.edit(embed=embed3)
            await asyncio.sleep(random.randint(1,3))
            embed1 = discord.Embed(title="**Success**" , description=f"{ctx.author.mention} have successfully steal nitro from <@{member.id}> \n **your nitro will last for {random.randint(1,60)} minutes**")
            embed1.set_footer(icon_url=ctx.author.display_avatar.url , text=f"Commands ran by {ctx.author.name}")
            await message.edit(embed=embed1)
        else:
            embed4 = discord.Embed(title="Failed :sob:" , description=f"Fail to steal nitro from {member.mention}" , timestamp=datetime.datetime.now())
            embed4.set_footer(icon_url=ctx.author.display_avatar.url , text=f"Commands ran by {ctx.author.name}")
            await message.edit(embed=embed4)
            take2 = random.randint(1,2)
            if take2 == 1:
                await asyncio.sleep(1)
                embed5 = discord.Embed(title="Failed :sob:" , description=f"Fail to steal nitro from {member.mention} \n but instead {member.mention} steal {ctx.author.mention}'s nitro \n **and the nitro will last for {random.randint(1,60)} minutes**" , timestamp=datetime.datetime.now())
                embed5.set_footer(icon_url=ctx.author.display_avatar.url , text=f"Commands ran by {ctx.author.name}")
                await message.edit(embed=embed5)
    @stealp.error
    async def error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            return
    
async def setup(bot):
    await bot.add_cog(stealnitro(bot))