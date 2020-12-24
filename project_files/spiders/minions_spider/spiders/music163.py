import scrapy
from scrapy_splash import SplashRequest


class hero(scrapy.Spider):
    name = "music_163"
    start_urls = [
        "http://music.163.com/discover/playlist/?order=hot"
    ]

    def parse(self, response, **kwargs):
        # selector = Selector(response.body)
        dicscs = response.selector.xpath("//p[@class='dec']/a")
        herf = 'http://music.163.com' + dicscs[0].attrib['href']

        yield SplashRequest(url=herf, callback=self.parse_song)

    def parse_song(self, response, **kwargs):
        songs = response.selector.xpath("//span[@class='txt']/a")
        # url = 'http://music.163.com' + songs[0].attrib['href']
        url = 'http://music.163.com/song?id=1452439191'
        yield scrapy.Request(url=url, callback=self.parse_suggest)

    def parse_suggest(self, response, **kwargs):
        all_comment = response.selector.xpath("//div[@class='cmmts j-flag']")

        print("debug")
