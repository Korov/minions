import scrapy
import requests as rs
from Crypto.Cipher import AES
import base64
import json
import os
import time

# 参考https://github.com/niechaojun/NetEaseCloudCrawer
class hero(scrapy.Spider):
    name = "music_163"
    start_urls = [
        "http://music.163.com/discover/playlist/?order=hot"
    ]

    def Nie_get_params(self, id, PageNum, Count):
        PageNum = (PageNum - 1) * 20
        first_param = "{ rid: \"R_SO_4_" + str(id) + "\", offset: " + str(
            PageNum) + ", total: \"false\", limit: " + str(Count) + ", csrf_token: \"\" }"
        forth_param = "0CoJUm6Qyw8W8jud"
        first_key = forth_param
        second_key = 'nienienienienien'
        h_encText = self.AES_encrypt(key=first_key, text=first_param)
        h_encText = self.AES_encrypt(key=second_key, text=h_encText)
        return h_encText.decode()

    def AES_encrypt(self, key, text):
        iv = '0102030405060708'
        # pad = 16 - len(text) % 16
        # text += str(pad * chr(pad).encode())
        while len(text) % 16 != 0:  # 补足字符串长度为16的倍数
            text += (16 - len(text) % 16) * chr(16 - len(text) % 16)
        # text = str.encode(text)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        encrypt_text = base64.b64encode(encrypt_text)
        return encrypt_text

    def Nie_get_encSecKey(self):
        encSrcKey = "6469da86a183fc2fc9df65ac98f67138c8d3048d0626714fe646ecb564d4f8cd386a9c9618bb8a4f2929e50ba32e8991266aba783975e39cc7cf8a61cc3ba76c81c64a3414f38d604ca1bf9f4647c29cd92d5b362eff15cf7bb1e3a52df798a52aafac2f09420a68af9686e2c1a294ccf426b5aac64899486011fc7eca8e79b8"
        return encSrcKey

    def N_comment(self, id, ReviewCount):
        ReviewKeep = 0
        KeepFile = os.getcwd() + os.sep + str(id) + ".nie"
        fp = open(KeepFile, 'w')
        PageNum = int(ReviewCount / 100)
        Count = 100
        if ReviewCount % 100 != 0:
            PageNum += 1
        for RP in range(1, PageNum + 1):
            if RP == PageNum:
                Count = ReviewCount % 100
            data = {
                'params': self.Nie_get_params(id, RP, Count),
                'encSecKey': self.Nie_get_encSecKey()
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
                'Cookie': 'JSESSIONID-WYYY=vDeNaw5OspW8kcNaX%5CsngVIwR3Z%2FigZ0HHGIb2duQgPm%2FFhGpQs6c26bKN3xf9tOatRbKk1JlTpJCiNsrZCsACk%2BN296WbpNc%2Fn96i8Ih6NYvHkjqXRR165SZAxv9YkkSAzfH9WTgCnyJUV6PEB9mm%2BJsduyy0B%5Cf2S7zXIdbls2hHY7%3A1519467798967; _iuqxldmzr_=32; _ntes_nnid=fc7bf97086aab1c7e5ea7559945fc3fe,1519465998987; _ntes_nuid=fc7bf97086aab1c7e5ea7559945fc3fe; __utma=94650624.1089055467.1519466000.1519466000.1519466000.1; __utmz=94650624.1519466000.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ngd_tid=izuEtMCQO5AHgNjd7VBI%2FItSs427hfCz',
            }
            url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_" + str(id) + "?csrf_token="
            r1 = rs.post(url, headers=headers, data=data).content
            json_1 = json.loads(r1)
            if "hotComments" in json_1:
                fp.write("最热评论:" + '\r\n')
                print
                u"最热评论" + str(len(json_1["hotComments"]))
                for i in range(0, len(json_1["hotComments"]) - 1):
                    HotReview = json_1["hotComments"][i]['user']['nickname'] + " : " + json_1["hotComments"][i][
                        'content'] + " (" + str(json_1["hotComments"][i]['likedCount']) + ") " + time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime(float(str(json_1['hotComments'][i]['time'])[0:10])))
                    print
                    HotReview
                    fp.write(HotReview.encode('utf-8') + '\r\n')
                    print
                fp.write("最新评论:" + '\r\n')
            print
            print
            u"最新评论" + str(len(json_1['comments']))
            ReviewKeep += len(json_1['comments'])
            for i in range(0, len(json_1['comments'])):
                NewReview = json_1['comments'][i]['user']['nickname'] + " : " + json_1['comments'][i][
                    'content'] + " (" + str(json_1["comments"][i]['likedCount']) + ") " + time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(float(str(json_1['comments'][i]['time'])[0:10])))
                print
                NewReview
                fp.write(NewReview.encode('utf-8') + '\r\n')
                print
        fp.close()
        print
        str(ReviewKeep) + u" 条评论已经保存在 " + KeepFile

    def parse(self, response, **kwargs):
        # selector = Selector(response.body)
        dicscs = response.selector.xpath("//p[@class='dec']/a")
        herf = 'http://music.163.com' + dicscs[0].attrib['href']

        yield scrapy.Request(url=herf, callback=self.parse_song)

    def parse_song(self, response, **kwargs):
        songs = response.selector.xpath("//ul[@class='f-hide']//li/a")
        for song in songs:
            song_id = str(song.attrib['href']).split('=')[1]
            self.N_comment(id=song_id, ReviewCount=10)
            print('debug')
        # yield scrapy.FormRequest(url=url, formdata={
        #     'params': 'RlBC7U1bfy/boPwg9ag7/a7AjkQOgsIfd+vsUjoMY2tyQCPFgnNoxHeCY+ZuHYqtM1zF8DWIBwJWbsCOQ6ZYxBiPE3bk+CI1U6Htoc4P9REBePlaiuzU4M3rDAxtMfNN3y0eimeq3LVo28UoarXs2VMWkCqoTXSi5zgKEKbxB7CmlBJAP9pn1aC+e3+VOTr0',
        #     'encSecKey': '76a0d8ff9f6914d4f59be6b3e1f5d1fc3998317195464f00ee704149bc6672c587cd4a37471e3a777cb283a971d6b9205ce4a7187e682bdaefc0f225fb9ed1319f612243096823ddec88b6d6ea18f3fec883d2489d5a1d81cb5dbd0602981e7b49db5543b3d9edb48950e113f3627db3ac61cbc71d811889d68ff95d0eba04e9'},
        #                          callback=self.parse_suggest)

    def parse_suggest(self, response, **kwargs):
        all_comment = response.selector.xpath("//div[@class='cmmts j-flag']")

        print("debug")
