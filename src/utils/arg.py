import nextcord
from nextcord.ext import commands
from utils.handler.getprefix import get_prefix

bot = commands.Bot(help_command=None , intents=nextcord.Intents.all() , command_prefix=get_prefix)
token = "";
owner = "";