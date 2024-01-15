import os , json

def get_prefix(bot , message) -> str:

    with open(os.path.dirname(__file__) + "/../../storage/prefix.json" , "r") as f:
        prefix = json.load(f)
    
    return prefix[str(message.guild.id)]