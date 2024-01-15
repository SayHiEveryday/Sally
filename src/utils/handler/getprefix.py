import os , json , aiosqlite

def get_prefix(bot , message) -> str:

    with open(os.path.dirname(__file__) + "/../../storage/prefix.json" , "r") as f:
        prefix = json.load(f)
                
    return prefix[str(message.guild.id)]

async def sql_get_prefix(bot, message):
    async with aiosqlite.connect("storage/prefix.sqlite") as db:
        query = f"SELECT * FROM prefix WHERE guild = {message.guild.id}"
        async with db.execute(query) as cursor:
            result = await cursor.fetchone()
            return str(result[1]) if result else "s!"
        