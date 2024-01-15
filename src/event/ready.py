import discord , json, os
from discord.ext import commands
from storage.arg import bot


class ready(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name=f"/help | {len(bot.guilds)} Servers!")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await bot.tree.sync()
        prefix_file_path = "storage/prefix.json"
        with open(prefix_file_path, "r") as p:
            prefix = json.load(p)

        # Check and update the prefix for each guild
        for g in bot.guilds:
            if str(g.id) not in prefix:
                prefix[str(g.id)] = "s!"

        # Save the updated prefix data back to the file
        with open(prefix_file_path, "w") as f:
            json.dump(prefix, f)

async def setup(bot):
    await bot.add_cog(ready(bot))