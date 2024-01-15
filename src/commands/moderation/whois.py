import discord , datetime
from discord.ext import commands
from discord import app_commands

class whois(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="whois" , description="Show basic info of mentioned user")
    async def whois_slash(self,interaction: discord.Interaction , member: discord.Member):
        match member.status:
            case discord.Status.online:
                c = 0x3BA55C
            case discord.Status.idle:
                c = 0xFAA61A
            case discord.Status.dnd:
                c = 0xED4245
            case discord.Status.offline:
                c = 0x747F8D
        jnat = datetime.datetime.strptime(str(member.joined_at), "%Y-%m-%d %H:%M:%S.%f%z")
        jnat2 = int(jnat.timestamp())
        rgat = datetime.datetime.strptime(str(member.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
        rgat2 = int(rgat.timestamp())

        embed = discord.Embed(title=f"Basic infomation of {member.display_name}",colour=c , timestamp=datetime.datetime.now())
        embed.add_field(name="User:" , value=f"{member.name}" , inline=True)
        embed.add_field(name="Join at:" , value=f"<t:{jnat2}:F>" , inline=True)
        embed.add_field(name="Registerd at:" , value=f"<t:{rgat2}:F>" , inline=True)
        embed.add_field(name="Role[" + str(len(member.roles)) + "]" , value=f",".join([f"<@&{r.id}>" for r in member.roles]) , inline=False)
        embed.set_author(name=f"Command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"id: {member.id}")

        await interaction.response.send_message(embed=embed)

    @commands.command(name="whois")
    async def whois_prefix(self,ctx: commands.Context , member: discord.Member):
        match member.status:
            case discord.Status.online:
                c = 0x3BA55C
            case discord.Status.idle:
                c = 0xFAA61A
            case discord.Status.dnd:
                c = 0xED4245
            case discord.Status.offline:
                c = 0x747F8D

        jnat = datetime.datetime.strptime(str(member.joined_at), "%Y-%m-%d %H:%M:%S.%f%z")
        jnat2 = int(jnat.timestamp())
        rgat = datetime.datetime.strptime(str(member.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
        rgat2 = int(rgat.timestamp())

        embed = discord.Embed(title=f"Basic infomation of {member.display_name}",colour=c , timestamp=datetime.datetime.now())
        embed.add_field(name="User:" , value=f"{member.name}" , inline=True)
        embed.add_field(name="Join at:" , value=f"<t:{jnat2}:F>" , inline=True)
        embed.add_field(name="Registerd at:" , value=f"<t:{rgat2}:F>" , inline=True)
        embed.add_field(name="Role[" + str(len(member.roles)) + "]" , value=f",".join([f"<@&{r.id}>" for r in member.roles]) , inline=False)
        embed.set_author(name=f"Command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"id: {member.id}")
        await ctx.reply(embed=embed)

    @whois_prefix.error
    async def error(self,ctx , error):
        if isinstance(error , commands.MissingRequiredArgument):
            match ctx.author.status:
                case discord.Status.online:
                    c = 0x3BA55C
                case discord.Status.idle:
                    c = 0xFAA61A
                case discord.Status.dnd:
                    c = 0xED4245
                case discord.Status.offline:
                    c = 0x747F8D
            jnat = datetime.datetime.strptime(str(ctx.author.joined_at), "%Y-%m-%d %H:%M:%S.%f%z")
            jnat2 = int(jnat.timestamp())
            rgat = datetime.datetime.strptime(str(ctx.author.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
            rgat2 = int(rgat.timestamp())

            embed = discord.Embed(title=f"Basic infomation of {ctx.author.display_name}",colour=c , timestamp=datetime.datetime.now())
            embed.add_field(name="User:" , value=f"{ctx.author.name}" , inline=True)
            embed.add_field(name="Join at:" , value=f"<t:{jnat2}:F>" , inline=True)
            embed.add_field(name="Registerd at:" , value=f"<t:{rgat2}:F>" , inline=True)
            embed.add_field(name="Role[" + str(len(ctx.author.roles)) + "]" , value=f",".join([f"<@&{r.id}>" for r in ctx.author.roles]) , inline=False)
            embed.set_author(name=f"Command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            embed.set_thumbnail(url=ctx.author.display_avatar.url)
            embed.set_footer(text=f"id: {ctx.author.id}")
            await ctx.reply(embed=embed)
async def setup(bot):
    await bot.add_cog(whois(bot))