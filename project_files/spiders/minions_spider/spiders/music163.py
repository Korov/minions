import random
import time

import scrapy
import requests as rs
from Crypto.Cipher import AES
import base64
import json
import logging
from minions_spider.kafkatool import kafka_producer

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
        return h_encText

    def AES_encrypt(self, key, text):
        iv = '0102030405060708'
        pad = 16 - len(text) % 16
        text = text + (pad * chr(pad))
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        encrypt_text = base64.b64encode(encrypt_text)
        return encrypt_text.decode('utf-8')

    def Nie_get_encSecKey(self):
        encSrcKey = "6469da86a183fc2fc9df65ac98f67138c8d3048d0626714fe646ecb564d4f8cd386a9c9618bb8a4f2929e50ba32e8991266aba783975e39cc7cf8a61cc3ba76c81c64a3414f38d604ca1bf9f4647c29cd92d5b362eff15cf7bb1e3a52df798a52aafac2f09420a68af9686e2c1a294ccf426b5aac64899486011fc7eca8e79b8"
        return encSrcKey

    def get_total_review_count(self, id):
        data = {
            'params': self.Nie_get_params(id, 1, 20),
            'encSecKey': self.Nie_get_encSecKey()
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Cookie': 'JSESSIONID-WYYY=vDeNaw5OspW8kcNaX%5CsngVIwR3Z%2FigZ0HHGIb2duQgPm%2FFhGpQs6c26bKN3xf9tOatRbKk1JlTpJCiNsrZCsACk%2BN296WbpNc%2Fn96i8Ih6NYvHkjqXRR165SZAxv9YkkSAzfH9WTgCnyJUV6PEB9mm%2BJsduyy0B%5Cf2S7zXIdbls2hHY7%3A1519467798967; _iuqxldmzr_=32; _ntes_nnid=fc7bf97086aab1c7e5ea7559945fc3fe,1519465998987; _ntes_nuid=fc7bf97086aab1c7e5ea7559945fc3fe; __utma=94650624.1089055467.1519466000.1519466000.1519466000.1; __utmz=94650624.1519466000.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ngd_tid=izuEtMCQO5AHgNjd7VBI%2FItSs427hfCz',
        }
        url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_" + str(id) + "?csrf_token="
        r1 = rs.post(url, headers=headers, data=data).content
        json_1 = json.loads(r1.decode('utf-8'))
        total_review_count = json_1.get('total')
        if total_review_count is None:
            return 0
        else:
            return total_review_count

    def send_comment(self, id):
        total_count = self.get_total_review_count(id)
        page_size = 20
        page_num = int(total_count / page_size)
        if total_count % page_size != 0:
            page_num += 1
        for start_page in range(1, page_num + 1):
            if start_page == page_num:
                page_size = total_count % page_size
            data = {
                'params': self.Nie_get_params(id, start_page, page_size),
                'encSecKey': self.Nie_get_encSecKey()
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
                'Cookie': 'JSESSIONID-WYYY=vDeNaw5OspW8kcNaX%5CsngVIwR3Z%2FigZ0HHGIb2duQgPm%2FFhGpQs6c26bKN3xf9tOatRbKk1JlTpJCiNsrZCsACk%2BN296WbpNc%2Fn96i8Ih6NYvHkjqXRR165SZAxv9YkkSAzfH9WTgCnyJUV6PEB9mm%2BJsduyy0B%5Cf2S7zXIdbls2hHY7%3A1519467798967; _iuqxldmzr_=32; _ntes_nnid=fc7bf97086aab1c7e5ea7559945fc3fe,1519465998987; _ntes_nuid=fc7bf97086aab1c7e5ea7559945fc3fe; __utma=94650624.1089055467.1519466000.1519466000.1519466000.1; __utmz=94650624.1519466000.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ngd_tid=izuEtMCQO5AHgNjd7VBI%2FItSs427hfCz',
            }
            url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_" + str(id) + "?csrf_token="
            time.sleep(random.randint(5,10))
            logging.info("total count {}, start page {}, pages size {}".format(total_count, start_page, page_size))
            r1 = rs.post(url, headers=headers, data=data).content
            json_1 = json.loads(r1.decode('utf-8'))
            kafka_producer.send_msg(topic='music_163', key=id, msg=json.dumps(json_1, ensure_ascii=False))


    def parse(self, response, **kwargs):
        dicscs = response.selector.xpath("//p[@class='dec']/a")
        for dicsc in dicscs:
            herf = 'http://music.163.com' + dicsc.attrib['href']
            yield scrapy.Request(url=herf, callback=self.parse_song)

    def parse_song(self, response, **kwargs):
        songs = response.selector.xpath("//ul[@class='f-hide']//li/a")
        end_index = 5
        if len(songs) < end_index:
            end_index = len(songs)
        for index in range(0, end_index):
            song = songs[index]
            song_id = str(song.attrib['href']).split('=')[1]
            self.send_comment(id=song_id)



