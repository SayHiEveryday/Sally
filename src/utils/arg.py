import nextcord , os , json
from nextcord.ext import commands
def get_prefix(bot , message):

    with open(os.path.dirname(__file__) + "/../utils/prefix.json" , "r") as f:
        prefix = json.load(f)
    
    return prefix[str(message.guild.id)]

bot = commands.Bot(help_command=None , intents=nextcord.Intents.all() , command_prefix=get_prefix)

token = "";
owner = "";