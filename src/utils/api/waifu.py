import requests
def wai() -> str:
    url = 'https://api.waifu.im/search'
    para = {
        'gif': "True",
        'is_nsfw': "True"
    }
    res = requests.get(url=url , params=para)
    photo = res.json()["images"]
    photo_url = (photo)[0]["url"]
    return photo_url