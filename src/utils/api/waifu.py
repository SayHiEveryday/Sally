import requests , random ,json
ran = ["True" , "False"]
def wai(nsfw):
    url = 'https://api.waifu.im/search'
    para = {
        'gif': ran[random.randint(0,1)],
        'is_nsfw': str(nsfw)
    }
    res = requests.get(url=url , params=para)
    photo = res.json()["images"]
    photo_url = (photo)[0]["url"]

    if photo[0]['artist'] is None:
        artist = "null"
    else:
        artist = photo[0]['artist']['name']
    
    infoj = {
        "source": photo[0]['source'],
        "url": photo[0]['url'],
        "artist": artist,
        "color": photo[0]['dominant_color']
    }
    info = json.dumps(infoj)
    return info
