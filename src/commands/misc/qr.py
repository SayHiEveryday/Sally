import qrcode,os
from discord.ext import commands
import discord
from discord import app_commands
class _qr(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def qr(self,ctx:commands.Context,text:str="example"):
        img = qrcode.make(text)
        img.save('qrcode.png')
        await ctx.send(file=discord.File('qrcode.png'))
        os.remove('qrcode.png')
    
    @app_commands.command(
        description="qrcode maker"
    )
    async def qrcode(self,interaction:discord.Interaction,text:str):
        img = qrcode.make(text)
        img.save('qrcodetemp.png')
        await interaction.response.send_message(file=discord.File('qrcodetemp.png'))
        os.remove('qrcodetemp.png')

async def setup(bot):
    await bot.add_cog(_qr(bot))