import nextcord
from nextcord.ext import commands
from utils.run import bot


class ready(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print("name: " + bot.user.name)
        print("id: " + str(bot.user.id))
        activity = nextcord.Game(name="/help")
        await bot.change_presence(status=nextcord.Status.idle, activity=activity)

def setup(bot):
    bot.add_cog(ready(bot))