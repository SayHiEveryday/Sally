import nextcord
import re
from nextcord.ext import commands

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                return commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                return commands.BadArgument("{} is not a number!".format(v))
        return time

class mute(commands.Cog):
    def __init__(self , client):
        super().__init__()

    @nextcord.slash_command(name="mute", description="timeout someone with inputed time",default_member_permissions=2)
    async def mute_slash(self,interaction: nextcord.Interaction , member: nextcord.Member , time:TimeConverter = nextcord.SlashOption(description="ex: 2d 10h 3m 2s maximium 7d"), reason: str = nextcord.SlashOption(default="Moderator did not put any reason")):
        try:
            await interaction.response.send_message("Done!")
            await member.timeout(timeout=time,reason=f"command ran by {interaction.user.name} with reason {reason}")
            await interaction.channel.send(embed=nextcord.Embed(description=f"{member.mention} is muted by {interaction.user.mention} with reason {reason}" , colour=nextcord.Color.blurple))
        except Exception as e:
            if "403" in str(e):
                await interaction.response.send_message("can't timeout this person")

    @commands.command(name="mute")
    @commands.has_permissions(kick_members=True)
    async def mute_prefix(self,ctx: commands.Context , member: nextcord.Member ,*, time:TimeConverter= None, reason = str):
        try:
            await ctx.message.delete()
            await member.timeout(timeout=time,reason=f"command ran by {ctx.author.name} with reason {reason}")
            await ctx.channel.send(embed=nextcord.Embed(description=f"{member.mention} is muted by {ctx.author.mention} with reason {reason}", colour=nextcord.Color.blurple))
        except Exception as e:
            if "403" in str(e):
                await ctx.reply("can't timeout this person")