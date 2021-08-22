import logging

import scrapy


class biquge(scrapy.Spider):
    name = "biquge"
    allowed_domains = ['xbiquge.la']

    def start_requests(self):
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"92\""
        }
        urls = [
            "https://www.xbiquge.la/xuanhuanxiaoshuo/"
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response, **kwargs):
        req = response.json()
        logging.info(req)
