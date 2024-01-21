import discord , discord.ext , ast
from discord.ext import commands
from utils.handler.logcmd import *

def insert_returns(body):
        # insert return stmt if the last expression is a expression statement
        if isinstance(body[-1], ast.Expr):
            body[-1] = ast.Return(body[-1].value)
            ast.fix_missing_locations(body[-1])

        # for if statements, we insert returns into the body and the orelse
        if isinstance(body[-1], ast.If):
            insert_returns(body[-1].body)
            insert_returns(body[-1].orelse)

        # for with blocks, again we insert returns into the body
        if isinstance(body[-1], ast.With):
            insert_returns(body[-1].body)

class evalcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="eval")
    async def eval_fn(self,ctx, *, cmd):
        logcmd(name=ctx.command,author=ctx.author,guild=ctx.guild,arg=cmd)
        if ctx.author.id == 698851209032761384:
            fn_name = "_eval_expr"

            cmd = cmd.strip("` ")

            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

            body = f"async def {fn_name}():\n{cmd}"

            parsed = ast.parse(body)
            body = parsed.body[0].body

            insert_returns(body)

            env = {
                'bot': ctx.bot,
                'discord': discord,
                'commands': commands,
                'ctx': ctx,
                '__import__': __import__
            }
            try:
                exec(compile(parsed, filename="<ast>", mode="exec"), env)

                result = (await eval(f"{fn_name}()", env))
            except Exception as e:
                await ctx.send(e)
        else:
            await ctx.reply("No superuser detected, Are you root?")
        
    @eval_fn.error
    async def error(self,ctx,error):
        if isinstance(error , commands.MissingRequiredArgument):
            if ctx.author.id == 698851209032761384:
                embed = discord.Embed(title="Result" , description="```undefinded```")
                await ctx.reply(embed=embed)
            else:
                await ctx.reply("No superuser detected, Are you root?")
async def setup(bot):
    await bot.add_cog(evalcmd(bot))
