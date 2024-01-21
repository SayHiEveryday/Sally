import aiosqlite
import discord
from discord.ext import commands

class sqlcall(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases=['sqlcall'])
    async def sql(self,ctx: commands.Context,path:str,*,prmp: str):
        if ctx.author.id != 698851209032761384:
            await ctx.reply("Permission Denied")
            return
        
        async with aiosqlite.connect(path) as db:
            try:
                c = await db.cursor()
                await c.execute(prmp)
                await db.commit()
                await ctx.reply("success")
            except Exception as e:
                await ctx.reply(str(e))

async def setup(bot):
    await bot.add_cog(sqlcall(bot))