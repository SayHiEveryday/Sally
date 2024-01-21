import json, requests

def rammore(get):
    return "https://rra.ram.moe" + json.loads(requests.get(f"https://rra.ram.moe/i/r?type={get}").text)['path']
