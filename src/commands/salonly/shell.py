import subprocess
import discord
from discord.ext import commands

class shell(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def shell(self,ctx,*, prompt):
        print(prompt)
        sayhi = 698851209032761384
        user = ctx.author.id
        if user == sayhi:
            output = subprocess.run(prompt, shell=True, capture_output=True, text=True)
            error = len(output.stderr)
            if error == 0:
                await ctx.reply(f"```{output.stdout}```")
            else:
                await ctx.reply(f"```{output.stderr}```")
        else:
            await ctx.reply('Error..., Missing Permission ')


async def setup(bot):
    await bot.add_cog(shell(bot))