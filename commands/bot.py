from flask_discord_interactions import DiscordInteractionsBlueprint, AsyncContext, Message
import datetime

botcommandbp = DiscordInteractionsBlueprint()

bot = botcommandbp.command_group("bot", is_async=True)

@bot.command(name="ping")
async def ping(ctx: AsyncContext):
    ping: int = int(datetime.datetime.now().timestamp() - ctx.message.timestamp.timestamp())
    async def do_followup():
        await ctx.edit(content="Pong! my latency is {0}".format(str(ping)))
    return Message(deferred=True)