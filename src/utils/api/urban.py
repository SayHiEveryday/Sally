import requests , json 

def urban(term):
    return json.loads(requests.get(f'https://api.urbandictionary.com/v0/define?term={term}').text)['list'][0]
