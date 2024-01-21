import discord , hashlib, os
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
        
        async with aiosqlite.connect("storage/settings.sqlite") as db:
            await db.execute("CREATE TABLE IF NOT EXISTS perguild ( guild varchar(255), nsfw varchar(1), UNIQUE(guild) )")
            await db.execute("CREATE TABLE IF NOT EXISTS peruser ( author varchar(255), UNIQUE(author) )")
            await db.commit()
            cursor = await db.cursor()
            for g in bot.guilds:
                try:
                    await cursor.execute(f"INSERT INTO perguild (guild,nsfw) VALUES ({g.id},'1')")
                    await db.commit()
                except Exception as e:
                    pass
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            cursor = await db.cursor()
            for g in bot.guilds:
                try:
                    await db.execute(f"CREATE TABLE IF NOT EXISTS {'t_'+str(g.id)} ( id varchar(255), mod varchar(255), tar varchar(255), reason varchar(255), UNIQUE(id) )")
                    await db.commit()
                except Exception as e:
                    print(e)
        async with aiosqlite.connect("storage/log.sqlite") as db:
            cursor = await db.cursor()
            for g in bot.guilds:
                try:
                    await db.execute(f"CREATE TABLE IF NOT EXISTS {'t_'+str(g.id)} ( id varchar(255), ty varchar(255) ,mod varchar(255), tar varchar(255), reason varchar(255), UNIQUE(id) )")
                    await db.commit()
                except Exception as e:
                    print(e)
            
        activity = discord.Game(name=f"/help | {len(bot.guilds)} Servers!")
        await bot.change_presence(status=discord.Status.online, activity=activity)
            

async def setup(bot):
    await bot.add_cog(ready(bot))
