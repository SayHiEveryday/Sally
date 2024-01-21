import discord , os
import discord.ext
from discord.ext import commands
from storage.arg import bot
import datetime
from discord import app_commands
from utils.handler.logcmd import *
import aiosqlite
from utils.handler.getprefix import sql_get_prefix
path = os.path.dirname(__file__) + "/../salonly/"

botre = """
`/help` - Show this embed
`/ping` - Show Latency between discord and the bot
`/stats` - Show Bot's Host specification
"""
Fun = """
`/fun`
    > `gay [member]` - Gay test a mention member
    > `8ball [question]` - Ask something
    > `impersonate [member][msg]` - Impersonate someone using webhook
    > `rps [choice]` - Play Rock Paper Scissor with bot
    > `stealnitro [member]` - Steal mentioned member's nitro
"""
Misc = """
`/serverinfo` - Show server basic infomation
`/history`
    > `today` - Show event today in the history
    > `thatday [month][day]` - Show event in the month and day you provide
`/qrcode` - Make a qrcode with text you provided
`/nsfw` - Nsfw commands
`/kitsu`
    > `search [type][name]` - Search anime/manga from kitsu.io
    > `random` - Return random anime
**--Prefix Only--**
`$emojisteal` - Return url of provided emoji
`$waifu` - Return image of waifu (nsfw module required)
`$waifu2` - Return image of waifu (nsfw module required)
"""
Mod = """
`/moderation`
    > `kick [member][reason]` - Kick a member
    > `ban [member][reason]` - Ban a member
    > `mute [member][time][reason]` - timeout a member
    > `unmute [member][reason]` - remove timeout
`/whois [member]` - Show basic user infomation
`/role`
    > `add [member][role]` - add role to mentioned member
    > `remove [member][role]` - remove role to mentioned member
`/nick`
    > `set` - Set a nickname to mentioned member
    > `clear` - Clear nickname to mentoned member
`/purge [amount]` - Clear message in the channel (max = 100)
`/avatar [member]` - Get avatar from mentioned member
"""
eco = """
`/economy`
    > `check [member]`- Check your balance
    > `work` - Work and get money
    > `give [member][amount]` - Give money to someone
    > `steal [member]` - Steal money from member
    > `leaderboard` - Show top 5 most money
"""

img = """
`/imagegen`
    > `hange_my_mine [text]` - Generate image about change my mind
    > `who_would_win [member]` - who would win
    > `kannagen [text]` - Generate kanna holding paper with inputed text
    > `trapcard [member]` - Make mentioned member stuck in trapcard
"""

setting = """
`/settings`
    > `nsfw [allowed]` - Allow nsfw related commands?
    > `prefix [new prefix]` - Server prefix
"""

emo = """
`/emote`
    > `hug [member]` - Someone being cute? hug them!
    > `kiss [member]` - Have feeling with someone? kiss them!
    > `pout [member]` - Send pout gif
    > `pat [member]` - Someone being cute? pat them!
    > `slap [member]` - dislike someone? slap them!
    > `cuddle [member]` - like someone? cuddle them!
    > `kill [member]` - Hate someone? Kill them!
    > `hug [member]` - 
"""

class dropdown(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Home",description="Go to home page"),
            discord.SelectOption(label="Bot Related",description="Show command related to bot"),
            discord.SelectOption(label="Fun" , description="Show command related to fun"),
            discord.SelectOption(label="Misc", description="Misc commands"),
            discord.SelectOption(label="Moderation",description="Show commands related to moderation"),
            discord.SelectOption(label="Economy",description="Commands related to economy"),
            discord.SelectOption(label="Emote",description="Emote commands"),
            discord.SelectOption(label="Image generation",description="Generate image (power by nekoapi)"),
            discord.SelectOption(label="Settings",description="Settings")
        ]
        super().__init__(placeholder="Select page that you need help",options=options,min_values=1,max_values=1)
    async def callback(self, interaction: discord.Interaction):
        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            query = "SELECT * FROM prefix WHERE guild = ?"
            async with db.execute(query, (str(interaction.guild.id),)) as cursor:
                result = await cursor.fetchone()
        match self.values[0]:
            case "Home":
                embed = discord.Embed(title=f"**Hey {interaction.user.name}!**", description=f"**You can find some useful link here**\n \n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally)\n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {result[1]}**",colour=0x5865F2,timestamp=datetime.datetime.now()).set_author(name=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
            case "Bot Related":
                embed = discord.Embed(title=f"**Bot Related**",description=botre,colour=discord.Colour.blurple())
            case "Fun":
                embed = discord.Embed(title=f"**Fun**",description=Fun,colour=discord.Colour.blurple())
            case "Misc":
                embed = discord.Embed(title=f"**Misc**",description=Misc.replace("$",result[1]),colour=discord.Colour.blurple())
            case "Moderation":
                embed = discord.Embed(title=f"**Moderation**",description=Mod,colour=discord.Colour.blurple())
            case "Economy":
                embed = discord.Embed(title=f"**Economy**",description=eco,colour=discord.Colour.blurple())
            case "Emote":
                embed = discord.Embed(title=f"**Emote**",description=emo,colour=discord.Colour.blurple())
            case "Image generation":
                embed = discord.Embed(title=f"**Image generation**",description=img,colour=discord.Colour.blurple())
            case "Settings":
                embed = discord.Embed(title=f"**Settings**",description=setting,colour=discord.Colour.blurple())

        await interaction.response.edit_message(embed=embed,view=prefixbutton())

class buttons(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.blurple, label=f"Total commands is {len(bot.tree.get_commands())}", disabled=True, custom_id="totalcmd",emoji=discord.PartialEmoji.from_str("<:question_mark:1171372577009176677>"))
    async def callback(self, interaction: discord.Interaction):
        pass

class prefixbutton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(dropdown())
        self.add_item(buttons())


class helpcmd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.bot = bot

    

    @app_commands.command(name="help" , description="View all commands")
    async def help_slash(self,interaction: discord.Interaction):        
        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            query = "SELECT * FROM prefix WHERE guild = ?"
            async with db.execute(query, (str(interaction.guild.id),)) as cursor:
                result = await cursor.fetchone()
        helpembed = discord.Embed(title=f"**Hey {interaction.user.name}!**", description=f"**You can find some useful link here**\n \n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally)\n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {result[1]}**",colour=0x5865F2,timestamp=datetime.datetime.now())
        await interaction.response.send_message(embed=helpembed.set_author(name=f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url) , view=prefixbutton())

    @commands.command(name="help")
    async def help_prefix(self,ctx):
        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            query = "SELECT * FROM prefix WHERE guild = ?"
            async with db.execute(query, (str(ctx.guild.id),)) as cursor:
                result = await cursor.fetchone()

        helpembed = discord.Embed(title=f"**Hey {ctx.author.name}!**", description=f"**You can find some useful link here**\n \n<:github:1171141412914466957> **Github**:\n[github.com](https://github.com/SayHiEveryday/Sally) \n<:gamejoy:1171141581252861962> **Ours discord server**: \n[discord.gg](https://discord.gg/hCvhq4md) \n<:question_mark:1171372577009176677> **My prefix for this server is: {result[1]}**",colour=0x5865F2,timestamp=datetime.datetime.now())
        await ctx.send(embed=helpembed.set_author(name=f"Command ran by {ctx.author.name}",icon_url=ctx.author.avatar.url) , view=prefixbutton())

async def setup(bot):
    await bot.add_cog(helpcmd(bot))