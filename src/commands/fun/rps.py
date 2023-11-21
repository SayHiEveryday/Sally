import nextcord 
from nextcord.ext import commands
from random import randint

rps_choice = ["rock" , "paper" , "scissor"]

class rps(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="rps" , description="Play Rock Paper Scissor with bot")
    async def rps_slash(self,interaction: nextcord.Interaction,choice=nextcord.SlashOption(name="choice",description="Your choice",choices=["rock" , "paper" , "scissor"],required=True)):
        randomed = rps_choice[randint(0,2)]
        if randomed == "rock" and choice == "rock":
            w = "Tie"
        elif randomed == "rock" and choice == "paper":
            w = "You win"
        elif randomed == "rock" and choice == "scissor":
            w = "You lose"
        elif randomed == "paper" and choice == "rock":
            w = "You lose"
        elif randomed == "paper" and choice == "paper":
            w = "Tie"
        elif randomed == "paper" and choice == "scissor":
            w = "You win"
        elif randomed == "scissor" and choice == "rock":
            w = "You win"
        elif randomed == "scissor" and choice == "paper":
            w = "You lose"
        elif randomed == "scissor" and choice == "scissor":
            w = "Tie"

        embed = nextcord.Embed(
            description=f"**Your choice: {choice}**\n**My choice: {randomed}**\n**Result: {w}**",
            colour=nextcord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)
    
def setup(bot):
    bot.add_cog(rps(bot))