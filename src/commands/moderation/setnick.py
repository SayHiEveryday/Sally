import discord , datetime , json , os
from discord.ext import commands
from discord import app_commands

class setnick(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    nick_slash = app_commands.Group(name="nick" , description="Set nickname for mentioned member" , default_permissions=134217728)

    @nick_slash.command(name="set" , description="Set nickname for mentioned member")
    async def nick_slash_set(interaction: discord.Interaction , member: discord.Member , new_nick:str):
        try:
            await member.edit(nick=new_nick)
            embed = discord.Embed(description=f"Nickname was changed for {member.mention}" , colour=discord.Color.random() , timestamp=datetime.datetime.now()).set_footer(text=f"command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
            await interaction.send(embed=embed)
        except Exception as e:
            if "403" in str(e):
                await interaction.send("can not change name for user that higher level than me or same level as me ")
                return

    @nick_slash.command(name="clear" , description="Clear nickname for mentioned member")
    async def nick_slash_set(self,interaction: discord.Interaction , member: discord.Member):
        try:
            await member.edit(nick=member.name)
            embed = discord.Embed(description=f"Nickname was cleared for {member.mention}" , colour=discord.Color.random() , timestamp=datetime.datetime.now()).set_footer(text=f"command ran by {interaction.user.name}" , icon_url=interaction.user.display_avatar.url)
            await interaction.send(embed=embed)
        except Exception as e:
            if "403" in str(e):
                await interaction.send("can not change name for user that higher level than me or same level as me ")
                return
    @commands.command(name="nick")
    @commands.has_permissions(manage_nicknames=True)
    async def nick_prefix(self,ctx, member: discord.Member, nick:str):
        try:
            await member.edit(nick=nick)
            embed = discord.Embed(description=f"Nickname was changed for {member.mention}" , colour=discord.Color.random() , timestamp=datetime.datetime.now()).set_footer(text=f"command ran by {ctx.author.name}" , icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)
        except Exception as e:
            if "403" in str(e):
                await ctx.send("can not change name for user that higher level than me or same level as me ")
                return
    @nick_prefix.error
    async def nick_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Hey! you don't have permission: `Manage_Nicknames`")
            return
        if isinstance(error,commands.MissingRequiredArgument):
            with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
                prefix = json.load(f)
                a = prefix[ctx.guild.id]
            embed = discord.Embed(
                title="How to use?",
                description=f"{a}nick [member][new nick]",
                colour=discord.Color.random()
            )
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(setnick(bot))