import scrapy


class hero(scrapy.Spider):
    name = "music_163"
    start_urls = [
        "http://music.163.com/discover/playlist/?order=hot"
    ]

    def _parse(self, response, **kwargs):
        print("start")
        print(response.url.split("/"))
        print("end")
