import requests
from bs4 import BeautifulSoup

class Pornhub:
    def __init__(self, query):
        self.query = query
        self.firstpage = 1

    def name(self):
        return 'Pornhub'

    def gif_url(self, page=None):
        page = page or self.firstpage
        return f'http://www.pornhub.com/gifs/search?search={self.query}&page={page}'



    def gif_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        gifs = soup.select('ul.gifs.gifLink li')

        return [
            {
                'title': gif.find('a').find('span').text,
                'url': f'http://dl.phncdn.com{gif.find("a").get("href")}.gif',
                'webm': gif.find('a').find('video').get('data-webm'),
            }
            for gif in gifs
        ]
