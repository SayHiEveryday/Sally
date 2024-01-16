import discord , json, os
from discord.ext import commands
from storage.arg import bot
import aiosqlite

class ready(commands.Cog):
    def __init__(self,client):
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.offline)

        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            await db.execute("CREATE TABLE IF NOT EXISTS prefix ( guild INT, prefix varchar(255),UNIQUE(guild) );")
            await db.commit()
            cursor = await db.cursor()
            for g in bot.guilds:
                try:
                    await cursor.execute(f"INSERT INTO prefix (guild,prefix) VALUES ({g.id},'s!')")
                    await db.commit()
                except:
                    pass

        async with aiosqlite.connect("storage/eco.sqlite") as db:
            await db.execute("CREATE TABLE IF NOT EXISTS eco ( name varchar(255), author INT, money varchar(255) );")
            await db.commit()
        
        activity = discord.Game(name=f"/help | {len(bot.guilds)} Servers!")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await bot.tree.sync()
            
async def setup(bot):
    await bot.add_cog(ready(bot))
