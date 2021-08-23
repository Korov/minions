import logging

import scrapy

from minions_spider.items import biquge_item


class biquge(scrapy.Spider):
    name = "biquge"
    allowed_domains = ['xbiquge.la']
    custom_settings = {
        'ITEM_PIPELINES': {'minions_spider.pipelines.biquge_pipeline': 300},
    }

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
        books = response.selector.xpath("//span[@class='s2']/a")
        authors = response.selector.xpath("//span[@class='s5']")
        for index in range(0, len(books)):
            book = books[index]
            book_id = str(book.attrib['href'])
            book_name = book.root.text
            author = authors[index]
            author_name = author.root.text
            my_item = biquge_item(book_url = book_id, book_name= book_name, author_name = author_name)
            yield my_item
