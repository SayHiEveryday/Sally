from discord.ext import commands
import discord , asyncio , random
from discord import app_commands
from utils.api.ram import rammore
from storage.arg import kill

class _emote(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    emo = app_commands.Group(name="emote",description="Just emote like hug pat.")

    @emo.command(name="hug" , description="Someone being cute? hug them!")
    async def hug_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> hug themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> hug robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} hug {member.name}!**").set_image(url=rammore("hug"))
        await interaction.followup.send(embed=embed)

    @emo.command(name="kiss" , description="Have feeling with someone? kiss them!")
    async def kiss_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> kiss themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> kiss robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} kiss {member.name}!**").set_image(url=rammore("kiss"))
        await interaction.followup.send(embed=embed)
    
    @emo.command(name="pout" , description="Send pout gif")
    async def pout_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            embed = discord.Embed(
                title=f"{interaction.user.name} pouts themself",
                colour=discord.Color.random(),
            ).set_image(
                url=rammore("pout")
            ).set_footer(
                text="command ran by {}".format(interaction.user.name),
                icon_url=interaction.user.display_avatar.url
            )
            await interaction.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            title=f"{interaction.user.name} pouts at {member.name}",
            colour=discord.Color.random()
        ).set_footer(
            text="command ran by {}".format(interaction.user.name),
            icon_url=interaction.user.display_avatar.url
        ).set_image(
            rammore("pout")
        )
        await interaction.response.send_message(embed=embed)
    
    @emo.command(name="pat" , description="Someone being cute? pat them!")
    async def pat_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> pat themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> pat robot but robot doesn't have feeling")
            return

        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} pat {member.name}!**").set_image(url=rammore("pat"))
        await interaction.followup.send(embed=embed)
    
    @emo.command(name="slap" , description="dislike someone? slap them!")
    async def slap_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> slap themself hope {interaction.user.name} is okay D:")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> slap robot but robot doesn't have feeling.")
            return

        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} slap {member.name}! , Hope {member.name} is okay D:**").set_image(url=rammore("slap"))
        await interaction.followup.send(embed=embed)

    @emo.command(name="cuddle" , description="like someone? cuddle them!")
    async def cuddle_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"Okay, <@{interaction.user.id}> cuddle themself")
            return
        
        if member.bot.real:
            await interaction.response.send_message(f"Okay seem like <@{interaction.user.id}> in love with robot")
            return
        
        await interaction.response.defer()
        embed = discord.Embed(title=f"**{interaction.user.name} cuddle {member.name}!**").set_image(url=rammore("cuddle"))
        await interaction.followup.send(embed=embed)

    @emo.command(name="kill" , description="Hate someone? Kill them!")
    async def kill_slash(self,interaction: discord.Interaction , member: discord.Member):
        if member.id == interaction.user.id:
            await interaction.response.send_message(f"<@{interaction.user.id}> killed themself")
            return
        if member.bot.real:
            await interaction.response.send_message(f"<@{interaction.user.id}> killed robot but robot come back and working perfectly fine")
            return
        
        await interaction.response.defer()
        await asyncio.sleep(2)
        await interaction.followup.send(kill[random.randint(0,185)].replace("$mention" , f"<@{member.id}>").replace("$author" , f"<@{interaction.user.id}>"))

    @commands.command(name="hug")
    async def hug_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> hug themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> hug robot but robot doesn't have feeling.")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} hug {member.name}!**").set_image(url=rammore("hug"))
        await ctx.send(embed=embed)

    @hug_prefix.error
    async def hug_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't hug air")

    @commands.command(name="cuddle")
    async def cuddle_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"Okay, <@{ctx.author.id}> cuddle themself")
            return
        if member.bot.real:
            await ctx.send(f"Okay seem like <@{ctx.author.id}> in love with robot")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} cuddle {member.name}!**").set_image(url=rammore("cuddle"))
        await ctx.send(embed=embed)
        
    @cuddle_prefix.error
    async def cuddle_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't cuddle air")

    @commands.command(name="pout")
    async def pout_prefix(self,ctx,member:discord.Member):
        embed = discord.Embed(
            title=f"{ctx.author.name} pouts at {member.name}",
            colour=discord.Color.random()
        ).set_footer(
            text="command ran by {}".format(ctx.author.name),
            icon_url=ctx.author.display_avatar.url
        ).set_image(
            url=rammore("pout")
        )
        await ctx.send(embed=embed)

    @pout_prefix.error
    async def pout_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title=f"{ctx.authot.name} pouts themself",
                colour=discord.Color.random(),
            ).set_image(
                url=rammore("pout")
            ).set_footer(
                text="command ran by {}".format(ctx.author.name),
                icon_url=ctx.author.display_avatar.url
            )
            await ctx.send(embed=embed)

    @commands.command(name="slap")
    async def slap_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> slap themself hope {ctx.author.name} is okay D:")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> slap robot but robot doesn't have feeling.")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} slap {member.name}! , Hope {member.name} is okay D:**").set_image(url=rammore("slap"))
        await ctx.send(embed=embed)

    @slap_prefix.error
    async def slap_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't slap air")

    @commands.command(name="pat")
    async def pat_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> pat themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> pat robot but robot doesn't have feeling.")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} pat {member.name}!**").set_image(url=rammore("pat"))
        await ctx.send(embed=embed)

    @pat_prefix.error
    async def pat_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! you can't pat air")
    
    @commands.command(name="kill")
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def kill_prefix(self,ctx , member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> killed themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> killed robot but robot come back and working perfectly fine")
            return
        
        await ctx.send(kill[random.randint(0,185)].replace("$mention" , f"<@{member.id}>").replace("$author" , f"<@{ctx.author.id}>"))

    @kill_prefix.error
    async def kill_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Ok you're dead. Please mention someone else to kill.")

    @commands.command(name="kiss")
    async def kiss_prefix(self,ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(f"<@{ctx.author.id}> kiss themself")
            return
        if member.bot.real:
            await ctx.send(f"<@{ctx.author.id}> kiss robot but robot doesn't have feeling.")
            return

        embed = discord.Embed(title=f"**{ctx.author.name} kiss {member.name}!**").set_image(url=rammore("kiss"))
        await ctx.send(embed=embed)

    @kiss_prefix.error
    async def kiss_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"{ctx.author.mention} kiss themself")

async def setup(bot):
    await bot.add_cog(_emote(bot))