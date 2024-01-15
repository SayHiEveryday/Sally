from discord.ext import commands
from storage.arg import bot
from discord import Embed , Color
from utils.handler.loadcogs import initial_extension
class synccmd(commands.Cog):
    def __init__(self, client) -> None:
        super().__init__()
        self.client = client
    
    @commands.command(name="sync")
    async def sync_prefix(self,ctx:commands.Context):
        if ctx.author.id == 698851209032761384:
            synced = await bot.tree.sync()
            await ctx.reply(embed=Embed(title=f"Synced {len(synced)} command",description="\n".join([f"</{s.name}:{str(s.id)}>" for s in synced]) , colour=Color.blurple()))
        else:
            return

async def setup(bot):
    await bot.add_cog(synccmd(bot))
