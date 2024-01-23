import aiosqlite , random , string
import discord
from discord.ext import commands
import datetime , humanfriendly
from discord import app_commands

class PaginationView(discord.ui.View):
    current_page : int = 1
    sep : int = 5
    og : int
    tar: str
    async def csend(self,ctx,tar):
        self.tar = tar.name
        self.og = ctx.author.id
        await ctx.send(view=self)
        self.message = await ctx.original_response()
        await self.update_message(self.data[:self.sep])

    async def send(self, ctx,tar):
        self.tar = tar.name
        self.og = ctx.user.id
        await ctx.response.send_message(view=self)
        self.message = await ctx.original_response()
        await self.update_message(self.data[:self.sep])

    def create_embed(self, data):
        embed = discord.Embed(title=f"Warnings for {self.tar} {self.current_page} / {int(len(self.data) / self.sep) + 1}",colour=discord.Color.blurple())
        for item in data:
            embed.add_field(name=item['label'], value=item['item'], inline=False)
        return embed

    async def update_message(self,data):
        self.update_buttons()
        await self.message.edit(embed=self.create_embed(data), view=self)

    def update_buttons(self):
        if self.current_page == 1:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == int(len(self.data) / self.sep) + 1:
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary

    def get_current_page_data(self):
        until_item = self.current_page * self.sep
        from_item = until_item - self.sep
        if not self.current_page == 1:
            from_item = 0
            until_item = self.sep
        if self.current_page == int(len(self.data) / self.sep) + 1:
            from_item = self.current_page * self.sep - self.sep
            until_item = len(self.data)
        return self.data[from_item:until_item]


    @discord.ui.button(label="|<",
                       style=discord.ButtonStyle.green)
    async def first_page_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.og:
            await interaction.response.send_message("Hey this button is not for you!")
            return
        
        await interaction.response.defer()
        
        self.current_page = 1

        await self.update_message(self.get_current_page_data())

    @discord.ui.button(label="<",
                       style=discord.ButtonStyle.primary)
    async def prev_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.og:
            await interaction.response.send_message("Hey this button is not for you!")
            return
        
        await interaction.response.defer()
        self.current_page -= 1
        await self.update_message(self.get_current_page_data())

    @discord.ui.button(label=">",
                       style=discord.ButtonStyle.primary)
    async def next_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.og:
            await interaction.response.send_message("Hey this button is not for you!")
            return
        
        await interaction.response.defer()
        self.current_page += 1
        await self.update_message(self.get_current_page_data())

    @discord.ui.button(label=">|",
                       style=discord.ButtonStyle.green)
    async def last_page_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.og:
            await interaction.response.send_message("Hey this button is not for you!")
            return
        await interaction.response.defer()
        self.current_page = int(len(self.data) / self.sep) + 1
        await self.update_message(self.get_current_page_data())



class _moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    mod = app_commands.Group(name="moderation",description="Moderation module")


    @mod.command(name="kick" , description="Kick a member")
    @app_commands.default_permissions(kick_members=True)
    async def _kick(self,interaction: discord.Interaction , member: discord.Member , reason: str = "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't kick a member who has administrator permission" , ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't kick a bot D:" , ephemeral=True)
            return
        if member.id == interaction.user.id:
            await interaction.response.send_message("Hey! you can't kick yourself" , ephemeral=True)
            return
        
        await interaction.response.send_message("Success" , ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been kicked | {reason}",colour=0x3BA55C)
        await member.kick(reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        await interaction.channel.send(embed=embed)


    @mod.command(name="ban" , description="Ban a member")
    @app_commands.default_permissions(ban_members=True)
    async def _ban(self,interaction: discord.Interaction , member: discord.Member , reason: str = "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't ban a member who has administrator permission" , ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't ban a bot D:" , ephemeral=True)
            return
        if member.id == interaction.user.id:
            await interaction.response.send_message("Hey! you can't ban yourself" , ephemeral=True)
            return
        
        await interaction.response.send_message("Success" , ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been banned | {reason}",colour=0x3BA55C)
        await member.ban(reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        await interaction.channel.send(embed=embed)

    @mod.command(name="mute",description="timeout a member")
    @app_commands.default_permissions(moderate_members=True)
    @app_commands.describe(
        member="member to timeout",
        time="duration ( 1d 2m 3s )",
        reason="reason to timeout"
    )
    async def _mute(self,interaction:discord.Interaction,member:discord.Member,time:str,reason:str= "Moderator didn't specific a reason"):
        if member.guild_permissions.administrator:
            await interaction.response.send_message("I can't mute a member who has administrator permission",ephemeral=True)
            return
        if member.bot.real:
            await interaction.response.send_message("i can't mute a bot D:" , ephemeral=True)
            return
        if member == interaction.user:
            await interaction.response.send_message("Hey! you can't mute yourself" , ephemeral=True)
            return
        try:
            r = humanfriendly.parse_timespan(time)
        except:
            await interaction.response.send_message(f"Invalid time. Example: `1d` `2m`",ephemeral=True)
            return
        
        try:
            await member.timeout(discord.utils.utcnow() + datetime.timedelta(seconds=r),reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        except:
            await interaction.response.send_message(f"Failed to mute {member.mention}",ephemeral=True)
            return
        await interaction.response.send_message("success",ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been muted for {time} | {reason}",colour=0x3BA55C)
        await interaction.channel.send(embed=embed)

    @mod.command(name="unmute",description="remove timeout from a member")
    @app_commands.default_permissions(moderate_members=True)
    async def _unmute(self,interaction:discord.Interaction,member: discord.Member,reason:str= "Moderator didn't specific a reason"):
        if not member.is_timed_out():
            await interaction.response.send_message(f"{member.mention} isn't muted",ephemeral=True)
            return
        try:
            await member.timeout(None,reason=f"Moderator: {interaction.user.name} , Reason: {reason}")
        except:
            await interaction.response.send_message(f"Fail to unmute {member.mention}",ephemeral=True)
            return
        await interaction.response.send_message("success",ephemeral=True)
        embed = discord.Embed(description=f"{member.name} has been unmuted | {reason}",colour=0x3BA55C)
        await interaction.channel.send(embed=embed)

    @mod.command(name="warn",description="warn a member")
    @app_commands.default_permissions(moderate_members=True)
    async def _warn(self,interaction: discord.Interaction, target: discord.Member , reason: str = "Moderator did not specific a reason"):
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            i = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
            cur = await db.cursor()
            await cur.execute(f"INSERT INTO {'t_'+str(interaction.guild.id)} (id,mod,tar,reason) VALUES ('{i}','{interaction.user.id}','{target.id}','{reason}')")
            await db.commit()
        await interaction.channel.send(embed=discord.Embed(description=f"{target.mention} has been warned | {reason}",colour=discord.Colour.random()))
        await interaction.response.send_message("warned",ephemeral=True)

    @mod.command(name="warnings",description="View warnings")
    @app_commands.default_permissions(moderate_members=True)
    async def _warnings(self,interaction:discord.Interaction,target:discord.Member):
        data = [

        ]
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            c = await db.cursor()
            r = await c.execute(f"SELECT * FROM {'t_'+str(interaction.guild.id)} WHERE tar = {target.id}")
            rows = await r.fetchall()
            if len(rows) == 0:
                await interaction.response.send_message(embed=discord.Embed(description=f"No record found for {target.mention}",colour=discord.Color.random()))
                return
        for row in rows:
            label = f"Warn id: {row[0]}"
            item = f"moderator: <@{row[1]}>\nreason: {row[3]}"
            data.append({"label": label, "item": item})
                
        pagination_view = PaginationView(timeout=None)
        pagination_view.data = data
        await pagination_view.send(interaction,target)

    @mod.command(name="delwarn",description="Delete warnings")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(id="warnings id")
    async def _delwarn(self,interaction:discord.Interaction,id:str):
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            c = await db.cursor()
            r = await c.execute(f"SELECT * FROM {'t_'+str(interaction.guild.id)} WHERE id = '{id}'")
            rows = r.fetchall()
            try:
                    len(rows)
            except:
                    await interaction.response.send_message("Error: {id} not found",ephemeral=True)
                    return
            await c.execute(f"DELETE FROM {'t_'+str(interaction.guild.id)} WHERE id = '{id}'")
            await db.commit()
            await interaction.response.send_message(f"deleted warnings id: {id} from database",ephemeral=True)



#prefix commands

    @commands.command(name="delwarn")
    async def _delwarn_(self,ctx: commands.Context,id:str):
        if not ctx.author.guild_permissions.administrator:
            await ctx.reply("You don't have permission to access this commands: `administrator`")
            return
        
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            c = await db.cursor()
            r = await c.execute(f"SELECT * FROM {'t_'+str(ctx.guild.id)} WHERE id = '{id}'")
            rows = r.fetchall()
            try:
                    len(rows)
            except:
                    await ctx.reply("Error: {id} not found",ephemeral=True)
                    return
            await c.execute(f"DELETE FROM {'t_'+str(ctx.guild.id)} WHERE id = '{id}'")
            await db.commit()
            await ctx.reply(f"deleted warnings id: {id} from database")


    @commands.command(name="warnings")
    async def _warnings_(self,ctx:commands.Context,target:discord.Member):
        if not ctx.author.guild_permissions.kick_members:
            await ctx.reply("You don't have permission to use this commands")
            return
        data = [

        ]
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            c = await db.cursor()
            r = await c.execute(f"SELECT * FROM {'t_'+str(ctx.guild.id)} WHERE tar = {target.id}")
            rows = await r.fetchall()
            if len(rows) == 0:
                await ctx.reply(embed=discord.Embed(description=f"No record found for {target.mention}",colour=discord.Color.random()))
                return
        for row in rows:
            label = f"Warn id: {row[0]}"
            item = f"moderator: <@{row[1]}>\nreason: {row[3]}"
            data.append({"label": label, "item": item})
                
        pagination_view = PaginationView(timeout=None)
        pagination_view.data = data
        await pagination_view.csend(ctx,target)

    @commands.command(name="warn")
    async def _warn_(self,ctx: commands.Context, target: discord.Member , reason: str = "Moderator didn't specific a reason"):
        async with aiosqlite.connect("storage/warn.sqlite") as db:
            i = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
            cur = await db.cursor()
            await cur.execute(f"INSERT INTO {'t_'+str(ctx.guild.id)} (id,mod,tar,reason) VALUES ({i},{ctx.author.id},{target.id},{reason})")
            await db.commit()
        await ctx.message.delete()
        await ctx.channel.send(embed=discord.Embed(description=f"{target.mention} has been warned | {reason}",colour=discord.Color.random()))
        

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban_prefix(self,ctx, member: discord.Member ,*, reason:str="Moderator didn't specific a reason"):
        if member == None:
            await ctx.reply("You need to mention a member to ban!")
            return
        if member.guild_permissions.administrator:
            await ctx.reply("I can't ban a member who have administrator permission")
            return
        if member.bot.real:
            await ctx.send("i can't ban a bot D:")
            return
        
        if member.id == ctx.author.id:
            await ctx.send("Hey! you can't ban yourself")
            return
        
        await ctx.message.delete()
        embed = discord.Embed(description=f"{member.name} has been banned | {reason}",colour=0x3BA55C)
        await member.ban(reason=f"Moderator: {ctx.author.name} , Reason: {reason}")
        await ctx.channel.send(embed=embed)

    @ban_prefix.error
    async def on_error(self,ctx , error):
        if isinstance(error , commands.MissingPermissions):
            await ctx.reply("Missing Permission: `ban_members`")
            return
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.reply(error)

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_prefix(self,ctx, member: discord.Member ,*, reason: str = "Moderator didn't specific a reason"):
        if member == None:
            await ctx.reply("You need to mention a member to kick")
            return
        if member.guild_permissions.administrator:
            await ctx.reply("I can't kick a member who have administrator permission")
            return
        if member.bot.real:
            await ctx.send("i can't kick a bot D:")
            return
        
        if member.id == ctx.author.id:
            await ctx.send("Hey! you can't kick yourself")
            return
        
        await ctx.message.delete()
        embed = discord.Embed(description=f"{member.name} has been kicked | {reason}",colour=0x3BA55C)
        await member.kick(reason=f"Moderator: {ctx.author.name} , Reason: {reason}")
        await ctx.channel.send(embed=embed)

    @kick_prefix.error
    async def on_error(self,ctx , error):
        if isinstance(error , commands.MissingPermissions):
            await ctx.reply("Missing Permission: `kick_members`")
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.reply(error)

async def setup(bot):
    await bot.add_cog(_moderation(bot))
