import discord , json, os
from discord.ext import commands
from storage.arg import bot
import aiosqlite

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

        async with aiosqlite.connect("storage/prefix.sqlite") as db:
            await db.execute("CREATE TABLE IF NOT EXISTS prefix ( guild INT, prefix varchar(255) );")
            await db.commit()
            cursor = await db.cursor()

            # Execute a query to fetch existing prefixes
            await cursor.execute("SELECT guild, prefix FROM prefix")

            # Fetch all rows
            rows = await cursor.fetchall()

            # Close the cursor
            await cursor.close()

        # Load existing prefixes into a dictionary
        prefix = {str(guild): prefix for guild, prefix in rows}

        # Update prefixes for guilds
        for g in bot.guilds:
            guild_id = str(g.id)
            if guild_id not in prefix:
                # Add default prefix for new guilds
                prefix[guild_id] = "s!"

                # Save updated prefixes back to the database
                async with aiosqlite.connect("storage/prefix.sqlite") as db:
                    # Create a cursor
                    cursor = await db.cursor()

                    # Execute a query to update prefixes
                    await cursor.executemany("INSERT OR IGNORE INTO prefix (guild, prefix) VALUES (?, ?)", prefix.items())

                    # Commit the changes
                    await db.commit()

                    # Close the cursor
                    await cursor.close()
            
async def setup(bot):
    await bot.add_cog(ready(bot))