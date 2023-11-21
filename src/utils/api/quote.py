import json , requests

def quote():
    return json.loads(requests.get("https://api.api-ninjas.com/v1/quotes", headers={'X-Api-Key': 'o6LhjnbOakeH6tKXMZ1OJA==jXuveAbMmClLIYDX'}).text)
