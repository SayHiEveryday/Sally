import discord , datetime
from discord.ext import commands
from utils.api.history import thatday,today
from discord import app_commands

class onthisday(commands.Cog):
    def __init__(self, client):
        self.client = client

    history = app_commands.Group(name="history" , description="Show what happened today in history")

    @history.command(name="today" , description="today date(UTC)")
    async def history_today(self,interaction: discord.Interaction):
        await interaction.response.defer()
        a = datetime.datetime.utcnow()
        b = a.strftime('%m/%d')
        link = today()['links']['0']['1']
        embed = discord.Embed(title=f"Today is {b} (UTC)" , description=f"**Text:** {today()['text']}".replace("&#8211;" , "~"), colour=0x5865F2)
        await interaction.followup.send(embed=embed)

    @history.command(name="thatday" , description="You can input a month and day to get history of that day")
    async def history_thatday(self,interaction: discord.Interaction , month:int , day:int):
        await interaction.response.defer()
        if month > 13:
            await interaction.followup.send("Month can only be up to 12" , ephemeral=True)
            return
        if day > 31:
            await interaction.followup.send("Day can only be up to 31" , ephemeral=True)
            return
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day >= 31:
                await interaction.followup.send("short months(month that has 30 day) can only be up to 30 day" , ephemeral=True)
                return
        link = thatday(month=month,day=day)['links']['0']['1']
        embed = discord.Embed(title=f"That day ({month} / {day})" , description=f"**Text:** {thatday(month=month,day=day)['text']}".replace("&#8211;" , "~"),colour=0x5865F2)
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(onthisday(bot))