from quart import Quart
from flask_discord_interactions import DiscordInteractions
import constant , os


from commands.bot import botcommandbp

app = Quart(__name__)
discord = DiscordInteractions(app)
discord.update_commands()

discord.register_blueprint(botcommandbp)

app.config["DISCORD_CLIENT_ID"] = constant.clientid
app.config["DISCORD_CLIENT_SECRET"] = constant.secret
app.config["DISCORD_PUBLIC_KEY"] = constant.publickey

discord.set_route_async("/interactions")
discord.verify_signature()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ['PORT']))