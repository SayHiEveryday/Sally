from flask_discord_interactions import DiscordInteractionsBlueprint, Message, Context, Embed
import requests

botcommandbp = DiscordInteractionsBlueprint()

bot = botcommandbp.command_group("bot")

@bot.command(name="ping")
def ping(ctx):
    return Message(content="Pong!")

@bot.command(name="info")
def info(ctx:Context):
    pass