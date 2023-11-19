import nextcord , datetime
from nextcord.ext import commands

class whois(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="whois" , description="Show basic info of mentioned user")
    async def whois_slash(self,interaction: nextcord.Interaction , member: nextcord.Member):
        jnat = datetime.datetime.strptime(str(member.joined_at), "%Y-%m-%d %H:%M:%S.%f%z")
        jnat2 = int(jnat.timestamp())
        rgat = datetime.datetime.strptime(str(member.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
        rgat2 = int(rgat.timestamp())

        embed = nextcord.Embed(title=f"Basic infomation of {member.display_name}",colour=0x5865F2 , timestamp=datetime.datetime.now())
        embed.add_field(name="User:" , value=f"{member.name}" , inline=True)
        embed.add_field(name="Join at:" , value=f"<t:{jnat2}:F>" , inline=True)
        embed.add_field(name="Registerd at:" , value=f"<t:{rgat2}:F>" , inline=True)
        embed.add_field(name="Role[" + str(len(member.roles)) + "]" , value=f",".join([f"<@&{r.id}>" for r in member.roles]) , inline=False)
        embed.set_author(name=f"Command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
        embed.set_thumbnail(member.display_avatar.url)
        embed.set_footer(text=f"id: {member.id}")

        await interaction.response.send_message(embed=embed)

    @commands.command(name="whois")
    async def whois_prefix(self,ctx , member: nextcord.Member):
        jnat = datetime.datetime.strptime(str(member.joined_at), "%Y-%m-%d %H:%M:%S.%f%z")
        jnat2 = int(jnat.timestamp())
        rgat = datetime.datetime.strptime(str(member.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
        rgat2 = int(rgat.timestamp())

        embed = nextcord.Embed(title=f"Basic infomation of {member.display_name}",colour=0x5865F2 , timestamp=datetime.datetime.now())
        embed.add_field(name="User:" , value=f"{member.name}" , inline=True)
        embed.add_field(name="Join at:" , value=f"<t:{jnat2}:F>" , inline=True)
        embed.add_field(name="Registerd at:" , value=f"<t:{rgat2}:F>" , inline=True)
        embed.add_field(name="Role[" + str(len(member.roles)) + "]" , value=f",".join([f"<@&{r.id}>" for r in member.roles]) , inline=False)
        embed.set_author(name=f"Command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(member.display_avatar.url)
        embed.set_footer(text=f"id: {member.id}")
        await ctx.reply(embed=embed)

    @whois_prefix.error
    async def error(self,ctx , error):
        if isinstance(error , commands.MissingRequiredArgument):
            jnat = datetime.datetime.strptime(str(ctx.author.joined_at), "%Y-%m-%d %H:%M:%S.%f%z")
            jnat2 = int(jnat.timestamp())
            rgat = datetime.datetime.strptime(str(ctx.author.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
            rgat2 = int(rgat.timestamp())

            embed = nextcord.Embed(title=f"Basic infomation of {ctx.author.display_name}",colour=0x5865F2 , timestamp=datetime.datetime.now())
            embed.add_field(name="User:" , value=f"{ctx.author.name}" , inline=True)
            embed.add_field(name="Join at:" , value=f"<t:{jnat2}:F>" , inline=True)
            embed.add_field(name="Registerd at:" , value=f"<t:{rgat2}:F>" , inline=True)
            embed.add_field(name="Role[" + str(len(ctx.author.roles)) + "]" , value=f",".join([f"<@&{r.id}>" for r in ctx.author.roles]) , inline=False)
            embed.set_author(name=f"Command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            embed.set_thumbnail(ctx.author.display_avatar.url)
            embed.set_footer(text=f"id: {ctx.author.id}")
            await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(whois(bot))