import os , json
from utils.arg import bot

def get_prefix(bot , message):

    with open(os.path.dirname(__file__) + "/../../utils/prefix.json" , "r") as f:
        prefix = json.load(f)
    
    return prefix[str(message.guild.id)]