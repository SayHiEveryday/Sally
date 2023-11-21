import requests , json , datetime , random
def today():
    today = datetime.datetime.utcnow()
    date = today.strftime('%m/%d')
    return json.loads(requests.get(url=f'https://today.zenquotes.io/api/{date}').text)["data"]["Events"][random.randint(0,20)]

def thatday(month,day):
    return json.loads(requests.get(url=f'https://today.zenquotes.io/api/{month}/{day}').text)["data"]["Events"][random.randint(0,20)]
