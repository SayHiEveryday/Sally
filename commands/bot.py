from flask_discord_interactions import DiscordInteractionsBlueprint, Message
import asyncio

botcommandbp = DiscordInteractionsBlueprint()

bot = botcommandbp.command_group("bot")

@bot.command(name="ping")
def ping(ctx):
    return Message(content="Pong!")