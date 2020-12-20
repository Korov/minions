import scrapy
from scrapy import Selector


class hero(scrapy.Spider):
    name = "music_163"
    start_urls = [
        "http://music.163.com/discover/playlist/?order=hot"
    ]

    def _parse(self, response, **kwargs):
        # selector = Selector(response.body)
        print(response)
        print("debug")
