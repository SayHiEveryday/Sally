import nextcord , json , os
from nextcord.ext import commands
from utils.run import bot



class guildjoin(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_guild_join(self,guild):

        with open("prefix.json" , "r") as f:
            prefix = json.load(f)

        prefix[str(guild.id)] = "s!"

        with open(os.path.dirname(__file__) + "/../utils/prefix.json" , "w") as f:
            json.dump(prefix , f)


def setup(bot):
    bot.add_cog(guildjoin(bot))