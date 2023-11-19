import nextcord , json , os
from nextcord.ext import commands

class change_prefix(commands.Cog):
    def __init__(self, client):
        self.client = client
    @nextcord.slash_command(name="change_prefix" , description="Change bot prefix" , default_member_permissions=8)
    async def changeprefix_slash(self,interaction: nextcord.Interaction , newprefix):
        with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
            prefix = json.load(f)

        prefix[str(interaction.guild.id)] = newprefix

        with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "w") as f:
            json.dump(prefix , f)

        await interaction.response.send_message(f"Prefix changed! new prefix: {newprefix}")

    @commands.command(name="change_prefix")
    @commands.has_permissions(administrator=True)
    async def changeprefix_prefix(self,ctx , newprefix):

        with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
            prefix = json.load(f)

        prefix[str(ctx.guild.id)] = newprefix

        with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "w") as f:
            json.dump(prefix , f)

        await ctx.send(f"Prefix changed! new prefix: {newprefix}")

    @changeprefix_prefix.error
    async def error(self,ctx,error):
        if isinstance(error , commands.MissingRequiredArgument):
            
            with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
                prefix = json.load(f)

            await ctx.reply(f"Hey what prefix are you going to change to , Your current prefix is **{prefix[str(ctx.guild.id)]}**")


def setup(bot):
    bot.add_cog(change_prefix(bot))