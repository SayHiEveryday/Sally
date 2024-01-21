from discord.ext import commands
from storage.arg import bot
from utils.handler.loadcogs import initial_extension

class reloadcmd(commands.Cog):
    def __init__(self, client) -> None:
        super().__init__()
        self.client = client

    @commands.command(name="reload",aliases=['re'])
    async def reload_cmd(self,ctx:commands.Context ,*, cmd:str):
        if ctx.author.id == 698851209032761384:
            try:
                await bot.reload_extension(cmd)
                await ctx.reply(f"reloaded {cmd}")
            except:
                await ctx.reply(f"{cmd} not found")
        else:
            return
        
    @reload_cmd.error
    async def reload_error(self,ctx,error):
        if ctx.author.id == 698851209032761384:
            for e in initial_extension:
                await bot.reload_extension(e)
            await ctx.reply(f"reloaded {len(initial_extension)} extension")
        else:
            return
async def setup(bot):
    await bot.add_cog(reloadcmd(bot))
