import nextcord
import nextcord.ext
from nextcord.ext import commands
import datetime

class purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="purge" , description="Delete message in the channel by amount" , default_member_permissions=8192)
    async def purge_slash(self,interaction: nextcord.Interaction , amount: int = nextcord.SlashOption(description="Amount maximium is 100")):
        if interaction.user.guild_permissions.manage_messages:
            if amount < 101:
                channel = interaction.channel
                deleted = await channel.purge(limit=amount)
                embed = nextcord.Embed(title=f'Deleted {len(deleted)} message(s)' , colour=0x5865F2 , timestamp=datetime.datetime.now()).set_footer(text=f"Commands ran by {interaction.user.name}" , icon_url=interaction.user.avatar.url)
                await channel.send(embed=embed , delete_after=5)
            else:
                await interaction.response.send_message("Maximium purge is 100" , ephemeral=True)
        else:
            await interaction.response.send_message("Lack of permission: `manage message`" , ephemeral=True)

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge_prefix(self,ctx, amount: int):
        if amount < 101:
            await ctx.message.delete()
            channel = ctx.channel
            deleted = await channel.purge(limit=amount)
            embed = nextcord.Embed(title=f'Deleted {len(deleted)} message(s)' , colour=0x5865F2 , timestamp=datetime.datetime.nowre()).set_footer(text=f"Commands ran by {ctx.user.name}" , icon_url=ctx.user.avatar.url)
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Maximium purge is 100" , ephemeral=True)

    @purge_prefix.error
    async def purge_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Hey! what are you gonna purge")
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Lack of permission: `manage message`")


def setup(bot):
    bot.add_cog(purge(bot))