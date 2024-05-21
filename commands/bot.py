from flask_discord_interactions import DiscordInteractionsBlueprint, Message, Context, Embed
import requests, constant, datetime

botcommandbp = DiscordInteractionsBlueprint()

bot = botcommandbp.command_group("bot")

@bot.command(name="info", description="Bot basic infomation")
def info(ctx:Context):
    re = requests.get(
        "https://discord.com/api/v10/users/@me/guilds",
        headers={"Authorization": "Bot " + constant.token}
    )
    guilds = len(re.json())
    embed = Embed(title="Bot Basic infomation",description=f"Bot is in {guilds} guilds")
    return Message(embed=embed)