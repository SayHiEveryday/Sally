import subprocess
import discord
from discord.ext import commands

class shell(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases=['syscall'])
    async def shell(self,ctx,*,prompt:str=None):

        if ctx.author.id == 698851209032761384:
            output = subprocess.run(prompt, shell=True, capture_output=True, text=True)
            error = len(output.stderr)
            out = len(output.stdout)
            if error == 0:
                if out == 0:
                    await ctx.reply("No output detected")
                else:
                    await ctx.reply(f"```{output.stdout}```")
            else:
                await ctx.reply(f"```{output.stderr}```")
        else:
            await ctx.reply("No superuser detected, Are you root?")


async def setup(bot):
    await bot.add_cog(shell(bot))