from flask import Flask

from flask_discord_interactions import DiscordInteractions
import constant , os, sys

from commands.bot import botcommandbp

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = constant.clientid
app.config["DISCORD_CLIENT_SECRET"] = constant.secret
app.config["DISCORD_PUBLIC_KEY"] = constant.publickey

@discord.command("hello")
def hello(ctx):
    return "Hello!"

discord.register_blueprint(botcommandbp)

discord.set_route("/interactions",app=app)

if "register" in sys.argv:
    discord.update_commands()
    sys.exit()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("port",443)), sslcontext=("fullchain.pem","privkey.pem"),debug=True)
