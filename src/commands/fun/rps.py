import discord 
from discord.ext import commands
from random import randint
from discord import app_commands

rps_choice = ["rock" , "paper" , "scissor"]

class rps(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="rps" , description="Play Rock Paper Scissor with bot")
    @app_commands.describe(choice="Your choice")
    @app_commands.choices(choice=[
        app_commands.Choice(name="rock" , value=0),
        app_commands.Choice(name="paper",value=1),
        app_commands.Choice(name="scissor",value=2)
    ])
    async def rps_slash(self,interaction: discord.Interaction,choice:discord.app_commands.Choice[int]):
        randomed = rps_choice[randint(0,2)]
        if randomed == "rock" and choice.name == "rock":
            w = "Tie"
        elif randomed == "rock" and choice.name == "paper":
            w = "You win"
        elif randomed == "rock" and choice.name == "scissor":
            w = "You lose"
        elif randomed == "paper" and choice.name == "rock":
            w = "You lose"
        elif randomed == "paper" and choice.name == "paper":
            w = "Tie"
        elif randomed == "paper" and choice.name == "scissor":
            w = "You win"
        elif randomed == "scissor" and choice.name == "rock":
            w = "You win"
        elif randomed == "scissor" and choice.name == "paper":
            w = "You lose"
        elif randomed == "scissor" and choice.name == "scissor":
            w = "Tie"

        embed = discord.Embed(
            description=f"**Your choice: {choice.name}**\n**My choice: {randomed}**\n**Result: {w}**",
            colour=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)
    
async def setup(bot):
    await bot.add_cog(rps(bot))