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

        yield scrapy.Request(url=herf, callback=self.parse_song)

    def parse_song(self, response, **kwargs):
        songs = response.selector.xpath("//ul[@class='f-hide']//li/a")
        # url = 'http://music.163.com' + songs[0].attrib['href']
        url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token='%(1340200924)
        yield scrapy.FormRequest(url=url, formdata= {'params': 'RlBC7U1bfy/boPwg9ag7/a7AjkQOgsIfd+vsUjoMY2tyQCPFgnNoxHeCY+ZuHYqtM1zF8DWIBwJWbsCOQ6ZYxBiPE3bk+CI1U6Htoc4P9REBePlaiuzU4M3rDAxtMfNN3y0eimeq3LVo28UoarXs2VMWkCqoTXSi5zgKEKbxB7CmlBJAP9pn1aC+e3+VOTr0', 'encSecKey': '76a0d8ff9f6914d4f59be6b3e1f5d1fc3998317195464f00ee704149bc6672c587cd4a37471e3a777cb283a971d6b9205ce4a7187e682bdaefc0f225fb9ed1319f612243096823ddec88b6d6ea18f3fec883d2489d5a1d81cb5dbd0602981e7b49db5543b3d9edb48950e113f3627db3ac61cbc71d811889d68ff95d0eba04e9'} ,callback=self.parse_suggest)

    def parse_suggest(self, response, **kwargs):
        all_comment = response.selector.xpath("//div[@class='cmmts j-flag']")

        print("debug")
