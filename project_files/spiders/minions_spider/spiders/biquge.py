import copy
import logging

import scrapy

from minions_spider.items import biquge_item

headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"92\""
}


class biquge(scrapy.Spider):
    name = "biquge"
    allowed_domains = ['xbiquge.la']
    custom_settings = {
        'ITEM_PIPELINES': {'minions_spider.pipelines.biquge_pipeline': 300},
    }

    def start_requests(self):
        urls = [
            "https://www.xbiquge.la/xuanhuanxiaoshuo/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse_books)

    def parse_books(self, response, **kwargs):
        books = response.selector.xpath("//span[@class='s2']/a")
        for book in books:
            book_url = str(book.attrib['href'])
            yield scrapy.Request(url=book_url, headers=headers, callback=self.parse_chapters)

    def parse_chapters(self, response, **kwargs):
        book_name = response.selector.xpath("//meta[@property='og:novel:book_name']")[0].attrib['content'].strip()
        book_description = response.selector.xpath("//meta[@property='og:description']")[0].attrib['content'].strip()
        book_category = response.selector.xpath("//meta[@property='og:novel:category']")[0].attrib['content'].strip()
        book_author = response.selector.xpath("//meta[@property='og:novel:author']")[0].attrib['content'].strip()
        book_url = response.selector.xpath("//meta[@property='og:novel:read_url']")[0].attrib['content'].strip()

        book_chapters = response.selector.xpath("//div[@id='list']/dl/dd/a")
        for book_chapter in book_chapters:
            chapter_url = 'https://www.xbiquge.la' + book_chapter.attrib['href']
            chapter_name = book_chapter.root.text.strip()
            book_item = biquge_item(book_name=book_name, book_description=book_description, book_category=book_category,
                                    book_author=book_author, book_url=book_url, chapter_url=chapter_url,
                                    chapter_name=chapter_name)
            yield scrapy.Request(url=chapter_url, headers=headers, meta={"item": book_item}, callback=self.parse_chapter)

    def parse_chapter(self, response, **kwargs):
        chapter_contents = response.selector.xpath("//div[@id='content']/text()")
        lines = []
        for line in chapter_contents:
            if line.root != '\r':
                lines.append(line.root.strip())
        item = response.meta['item']
        item['chapter_content'] = lines
        yield item
