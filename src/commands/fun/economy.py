from discord.ext import commands
import discord , aiosqlite , random
from discord import app_commands
class _economy(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    eco = app_commands.Group(name="economy",description="Economy")

    @eco.command(description="Check your money")
    async def check(self,interaction: discord.Interaction,*,member: discord.Member = None):
        if member is None:
            mem = interaction.user
        else:
            mem = member
        
        if mem.bot.real:
            await interaction.response.send_message(embed=discord.Embed(description="Error: Bot doesn't have economy account",colour=discord.Colour.random()))
            return
        async with aiosqlite.connect("storage/eco.sqlite") as db:
            c = await db.cursor()
            try:
                a = await c.execute(f"SELECT * FROM eco WHERE author = {mem.id}")
                t = await a.fetchone()
                embed = discord.Embed(description=f"Currently {mem.mention} have {t[2]}$",colour=discord.Color.random())
                await interaction.response.send_message(embed=embed)
            except:
                await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{mem.name}',{mem.id},'0')")
                await db.commit()
                embed = discord.Embed(description=f"Currently {mem.mention} have 0$",colour=discord.Color.random())
                await interaction.response.send_message(embed=embed)
            await c.close()
        
    
    @eco.command(description="Get money by working")
    async def work(self,interaction:discord.Interaction):
        await interaction.response.defer()
        randomize = random.randint(0,1000)
        async with aiosqlite.connect("storage/eco.sqlite") as db:
            c = await db.cursor()
            try:
                a = await c.execute(f"SELECT * FROM eco WHERE author = {interaction.user.id}")
                ogr = await a.fetchone()
                og = int(ogr[2])
                await c.execute(f"UPDATE eco SET money = {str(og + randomize)} WHERE author = {interaction.user.id}")
                await db.commit()
                embed = discord.Embed(description=f"Originally you have {str(og)}$\nYou have got {str(randomize)}$\nAnd now you now have {str(og + randomize)}$",colour=discord.Color.random())
                await interaction.followup.send(embed=embed)
            except Exception as e:
                embedd = discord.Embed(description=f"Originally you have 0$\nYou have got {randomize}$\nAnd now you now have {randomize}$",colour=discord.Color.random())
                await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{interaction.user.name}',{interaction.user.id},'{randomize}')")
                await db.commit()
                await interaction.followup.send(embed=embedd)
            await c.close()
    
    @eco.command(description="Give money to another member")
    async def give(self,interaction: discord.Interaction,member: discord.Member,amount:int):
        await interaction.response.defer()
        if member.bot.real:
            await interaction.followup.send(embed=discord.Embed(description="Error: Bot doesn't have economy account",colour=discord.Colour.random()))
            return
        
        async with aiosqlite.connect("storage/eco.sqlite") as db:
            c = await db.cursor()
            # author
            try:
                a = await c.execute(f"SELECT * FROM eco WHERE author = {interaction.user.id}")
                ori = await a.fetchone()
                o = int(ori[2])
                if amount > o:
                    await interaction.followup.send(embed=discord.Embed(description=f"Error: You cannot send more money than the amount you currently have; you have {o}$."))
                    return
            except:
                await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{interaction.user.name}',{interaction.user.id},'0')")
                await db.commit()
                await interaction.followup.send(embed=discord.Embed(description=f"Error: You cannot send more money than the amount you currently have; you have 0$."))
                return
            
            #member
            m = await c.execute(f"SELECT * FROM eco WHERE author = {member.id}")
            mm = await m.fetchone()
            try:
                rm = int(mm[2])
            except:
                await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{member.name}',{member.id},'0')")
                await db.commit()
                rm = 0

            #update author
            await c.execute(f"UPDATE eco SET money = {str(o - amount)} WHERE author = {interaction.user.id}")
            
            #update member
            tt = (rm + amount)
            await c.execute(f"UPDATE eco SET money = {str(tt)} WHERE author = {member.id}")
            await db.commit()

            embed = discord.Embed(description=f"{member.mention} have been given {int(tt)}$ from {interaction.user.mention}",colour=discord.Color.random())
            await interaction.followup.send(embed=embed)
    
    @eco.command(description="Steal people money")
    async def steal(self,interaction:discord.Interaction,member:discord.Member):
        await interaction.response.defer()
        if member.bot.real:
            await interaction.followup.send(embed=discord.Embed(description="Error: Bot doesn't have economy account",colour=discord.Colour.random()))
            return
        
        ran = random.randint(1,2)
        
        async with aiosqlite.connect("storage/eco.sqlite") as db:
            c = await db.cursor()
            if ran == 1: #success
                try:
                    a = await c.execute(f"SELECT * FROM eco WHERE author = {interaction.user.id}")
                    ori = await a.fetchone()
                    o = int(ori[2])
                except:
                    await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{interaction.user.name}',{interaction.user.id},'0')")
                    await db.commit()
                
                #member
                m = await c.execute(f"SELECT * FROM eco WHERE author = {member.id}")
                mm = await m.fetchone()
                try:
                    rm = int(mm[2])
                except:
                    await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{member.name}',{member.id},'0')")
                    await db.commit()
                    await interaction.followup.send(embed=discord.Embed(description=f"Error: {member.mention} doesn't have any money",colour=discord.Colour.random()))
                    return

                srand = random.randint(0,(int(rm * 0.7)))
                await c.execute(f"UPDATE eco SET money = '{rm - srand}' WHERE author = {member.id}")
                await c.execute(f"UPDATE eco SET money = '{o + srand}' WHERE author = {interaction.user.id}")
                await db.commit()
                embed = discord.Embed(description=f"{interaction.user.mention} has stolen {srand}$ from {member.mention}; now he/she have {o+srand}$",colour=discord.Color.random())
                await interaction.followup.send(embed=embed)
            else:
                try:
                    a = await c.execute(f"SELECT * FROM eco WHERE author = {interaction.user.id}")
                    ori = await a.fetchone()
                    o = int(ori[2])
                except:
                    await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{interaction.user.name}',{interaction.user.id},'0')")
                    await db.commit()
                    await interaction.followup.send(embed=discord.Embed(description=f"{interaction.user.mention} got caught while stealing but he/she doesn't have any money",colour=discord.Color.random()))
                    return
                
                #member
                m = await c.execute(f"SELECT * FROM eco WHERE author = {member.id}")
                mm = await m.fetchone()
                try:
                    rm = int(mm[2])
                except:
                    await c.execute(f"INSERT INTO eco (name,author,money) VALUES ('{member.name}',{member.id},'0')")
                    await db.commit()

                randd = random.randint(0,(int(o * 0.7)))
                await c.execute(f"UPDATE eco SET money = {o - randd} WHERE author = {interaction.user.id}")
                await c.execute(f"UPDATE eco SET money = {rm + randd} WHERE author = {member.id}")
                await db.commit()
                await interaction.followup.send(embed=discord.Embed(description=f"{interaction.user.mention} got caught while attemping to steal {member.mention}'s money so he/she lose {randd}$ current amount is {o - randd}$"))


async def setup(bot):
    await bot.add_cog(_economy(bot))