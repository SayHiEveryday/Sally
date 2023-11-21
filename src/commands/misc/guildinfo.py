import nextcord , datetime
from nextcord.ext import commands

class viewrole(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="View roles" , style=nextcord.ButtonStyle.blurple , custom_id="viewrole")
    async def viewrole(self , button: nextcord.Button , interaction: nextcord.Interaction):
        guild = interaction.guild
        embed = nextcord.Embed(description=f"\n".join([f"<@&{r.id}>" for r in guild.roles]))
        await interaction.response.send_message(embed=embed , ephemeral=True)
    
    @nextcord.ui.button(label="View emoji", style=nextcord.ButtonStyle.blurple , custom_id="viewemo")
    async def viewemo(self,button:nextcord.Button , interaction: nextcord.Interaction):
        try:
            guild = interaction.guild
            embed = nextcord.Embed(description="".join([f"{emoji}" for emoji in interaction.guild.emojis]))
            await interaction.response.send_message(embed=embed , ephemeral=True)
        except Exception as e:
            if "400" in str(e):
                await interaction.response.send_message("No emoji in this guild" , ephemeral=True)

    
class guildinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="guildinfo" , description="Get info of current guild")
    async def guildinfo_slash(self,interaction: nextcord.Interaction):

        if interaction.channel.type is nextcord.ChannelType.private:
            await interaction.response.send_message("you can only execute this command in guild")
            return

        guild = interaction.guild

        rgat = datetime.datetime.strptime(str(guild.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
        rgat2 = int(rgat.timestamp())
        
        embed = nextcord.Embed(title="**Basic guild infomation**" ,description=f"**Total Channels:** {str(len(guild.channels))}\n**Total roles:** {str(len(guild.roles))}\n**Total Member:** {str(guild.member_count)}\n**Total Bots:** {str(len(guild.bots))}", colour=0x5865F2 , timestamp=datetime.datetime.now())
        embed.add_field(name="Name:" , value=f"{guild.name}" , inline=True)
        embed.add_field(name="Create at:" , value=f"<t:{rgat2}:F>" , inline=True)
        embed.add_field(name="Owner:" , value=f"{guild.owner.mention}" , inline=True)
        embed.set_footer(text=f"ID: {guild.id}")
        embed.set_author(name=f"Command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
        if not guild.icon == None:
            embed.set_thumbnail(guild.icon.url)

        await interaction.response.send_message(embed=embed , view=viewrole())

    @commands.command(name="guildinfo")
    async def guildinfo_prefix(self,ctx):

        if ctx.channel.type is nextcord.ChannelType.private:
            await ctx.reply("you can only execute this command in guild")
            return
        
        guild = ctx.guild

        rgat = datetime.datetime.strptime(str(guild.created_at), "%Y-%m-%d %H:%M:%S.%f%z")
        rgat2 = int(rgat.timestamp())
        
        embed = nextcord.Embed(title="**Basic guild infomation**" ,description=f"**Total Channels:** {str(len(guild.channels))}\n**Total roles:** {str(len(guild.roles))}\n**Total Member:** {str(guild.member_count)}\n**Total Bots:** {str(len(guild.bots))}", colour=0x5865F2 , timestamp=datetime.datetime.now())
        embed.add_field(name="Name:" , value=f"{guild.name}" , inline=True)
        embed.add_field(name="Create at:" , value=f"<t:{rgat2}:F>" , inline=True)
        embed.add_field(name="Owner:" , value=f"{guild.owner.mention}" , inline=True)
        embed.set_footer(text=f"ID: {guild.id}")
        embed.set_author(name=f"Command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
        if not guild.icon == None:
            embed.set_thumbnail(guild.icon.url)

        await ctx.send(embed=embed , view=viewrole())

def setup(bot):
    bot.add_cog(guildinfo(bot))