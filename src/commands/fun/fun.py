from discord.ext import commands
import discord , datetime , random , asyncio
from discord import app_commands
from storage.arg import answer


class _fun(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

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
    fun = app_commands.Group(name="fun",description="commands related to fun")

    @fun.command(name="rps",description="Play Rock Paper Scissor with bot")
    @app_commands.describe(choice="Your choice")
    @app_commands.choices(choice=[
        app_commands.Choice(name="rock" , value=0),
        app_commands.Choice(name="paper",value=1),
        app_commands.Choice(name="scissor",value=2)
    ])
    async def rps_slash(self,interaction: discord.Interaction,choice:discord.app_commands.Choice[int]):
        rps_choice = ["rock" , "paper" , "scissor"]
        
        randomed = rps_choice[random.randint(0,2)]
        if randomed == "rock" and choice.name == "rock":
            w = "Tie"
        elif randomed == "rock" and choice.name == "paper":
            w = "You win"
        elif randomed == "rock" and choice.name == "scissor":
            w = "You lose"
        elif randomed == "paper" and choice.name == "rock":
            w = "You lose"
        elif randomed == "paper" and choice.name == "paper":
            w = "Tie"
        elif randomed == "paper" and choice.name == "scissor":
            w = "You win"
        elif randomed == "scissor" and choice.name == "rock":
            w = "You win"
        elif randomed == "scissor" and choice.name == "paper":
            w = "You lose"
        elif randomed == "scissor" and choice.name == "scissor":
            w = "Tie"

        embed = discord.Embed(
            description=f"**Your choice: {choice.name}**\n**My choice: {randomed}**\n**Result: {w}**",
            colour=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)
    
    @fun.command(name="gay",description="gay check for mentioned user")
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

    @fun.command(name="8ball" , description="Help decide a question")
    async def eightball_slash(self,interaction: discord.Interaction , question: str):
        num = random.randint(0,len(answer))


        await interaction.response.send_message(f"Question: **{question}**\nAnswer: `{answer[num]}` , <@{interaction.user.id}>")

    @commands.command(name="8ball")
    async def eightball_prefix(self,ctx ,*, question: str):
        num = random.randint(0,len(answer))

        await ctx.reply(f"Question: **{question}**\n Answer:`{answer[num]}` , <@{ctx.author.id}>")

    @eightball_prefix.error
    async def ball_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Missing Required Argument")

    @fun.command(name="impersonate" , description="impersonate someone with usage of webhook")
    @app_commands.describe(member="Member to impersonate",msg="Message to send")
    @app_commands.checks.cooldown(1,30,key=lambda i: (i.guild_id,i.user.id))
    async def impersonate_command(self,interaction: discord.Interaction , member: discord.Member , msg: str):
        if "@everyone" in msg:
            await interaction.response.send_message("you can not ping everyone with impersonate commands",ephemeral=True)
            return
        if "@here" in msg:
            await interaction.response.send_message("you can not ping here with impersonate commands",ephemeral=True)
            return
        if "<@&" in msg:
            await interaction.response.send_message("you can not ping role with impersonate commands",ephemeral=True)
            return
        
        await interaction.response.send_message(content="Sending message please wait",ephemeral=True)
        hook = await interaction.channel.create_webhook(name=member.display_name,reason=f"impersonate command on sally bot (created by {interaction.user.name})")
        await hook.send(content=msg,avatar_url=member.display_avatar.url)
        await hook.delete()
        a = await interaction.original_response()
        await a.edit(content=f"message sent! => {a.jump_url}")

    @impersonate_command.error
    async def err(self,interaction: discord.Interaction,error: app_commands.AppCommandError):
        if isinstance(error,app_commands.CommandOnCooldown):
            await interaction.response.send_message(error,ephemeral=True)
            return
        else:
            embed = discord.Embed(
                title="Please report this to the developer (username = sa.l)",
                description=f"```\n{error}\n```",
                colour=discord.Color.random()
            )
            await interaction.response.send_message(content="https://discord.gg/jWkknghvaz",embed=embed , ephemeral=True)

    @fun.command(name="stealnitro" , description="being poor? just steal other people nitro!")
    async def steals(self,interaction: discord.Interaction , member: discord.Member):
        if member.bot.real:
            await interaction.response.send_message("you can't steal bot nitro :skull: :skull: :skull: :skull:")
            return
        
        if member.id == interaction.user.id:
            await interaction.response.send_message("you can't steal your own nitro :skull: :skull: :skull: :skull:")
            return

        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(description="```checking user 1/3```")
            embed2 = discord.Embed(description="```stealing nitro 2/3 \n```")
            embed3 = discord.Embed(description=f"```sending nitro to {interaction.user.name} 3/3```")
            await interaction.response.send_message(embed=embed)
            await asyncio.sleep(random.randint(1,3))
            msg = await interaction.original_response()
            await msg.edit(embed=embed2)
            await asyncio.sleep(random.randint(1,3))
            take = random.randint(1,4)
            if take == 1:
                await asyncio.sleep(random.randint(1,3))
                await msg.edit(embed=embed3)
                await asyncio.sleep(random.randint(1,3))
                embed1 = discord.Embed(title="**Success**" , description=f"{interaction.user.mention} have successfully steal nitro from <@{member.id}> \n **your nitro will last for {random.randint(1,60)} minutes**")
                embed1.set_footer(icon_url=interaction.user.display_avatar.url , text=f"Commands ran by {interaction.user.name}")
                await msg.edit(embed=embed1)
            else:
                embed4 = discord.Embed(title="Failed :sob:" , description=f"Fail to steal nitro from {member.mention}")
                embed4.set_footer(icon_url=interaction.user.display_avatar.url , text=f"Commands ran by {interaction.user.name}")
                await msg.edit(embed=embed4)
                take2 = random.randint(1,2)
                if take2 == 1:
                    await asyncio.sleep(1)
                    embed5 = discord.Embed(title="Failed :sob:" , description=f"Fail to steal nitro from {member.mention} \n but instead {member.mention} steal {interaction.user.mention}'s nitro \n **and the nitro will last for {random.randint(1,60)} minutes**")
                    embed5.set_footer(icon_url=interaction.user.display_avatar.url , text=f"Commands ran by {interaction.user.name}")
                    await msg.edit(embed=embed5)
                    
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
    await bot.add_cog(_fun(bot))