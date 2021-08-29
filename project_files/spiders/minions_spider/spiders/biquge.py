import copy
import datetime
import time
from pymongo.mongo_client import MongoClient
import redis

import scrapy

from minions_spider.items import biquge_item

headers = {
    "Host": "www.xbiquge.la",
    "Connection": "keep-alive",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="92"',
    "sec-ch-ua-mobile": "?0",
    "Upgrade-Insecure-Requests": "Upgrade-Insecure-Requests",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
}

client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
db = client['spider']
collection = db['book_info']
redis_db = redis.Redis(host='korov.myqnapcloud.cn', port=6379, db=0)


class biquge(scrapy.Spider):
    name = "biquge"
    allowed_domains = ['xbiquge.la']
    custom_settings = {
        'ITEM_PIPELINES': {'minions_spider.pipelines.biquge_pipeline': 300},
        'DUPEFILTER_CLASS' : 'minions_spider.filters.BiqugeFilter',
        'DOWNLOAD_TIMEOUT': 120,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
        'DOWNLOAD_DELAY': 10,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,
        'AUTOTHROTTLE_MAX_DELAY': 60,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0
    }
    # 每次启动一个爬虫则所有url都要重新抢
    redis_db.delete("seen_urls")

    def start_requests(self):
        urls = [
            "https://www.xbiquge.la/dushixiaoshuo/",
            "https://www.xbiquge.la/xiuzhenxiaoshuo/",
            "https://www.xbiquge.la/dushixiaoshuo/",
            "https://www.xbiquge.la/chuanyuexiaoshuo/",
            "https://www.xbiquge.la/wangyouxiaoshuo/",
            "https://www.xbiquge.la/kehuanxiaoshuo/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse_books, priority=1)

    def parse_books(self, response, **kwargs):
        books = response.selector.xpath("//span[@class='s2']/a")
        for book in books:
            book_url = str(book.attrib['href'])
            yield scrapy.Request(url=book_url, headers=headers, callback=self.parse_chapters, priority=2)

        # 爬到最后一页的时候从第一页从新开始爬
        next_url = response.selector.xpath("//a[@class='next']")
        if len(next_url) == 1:
            yield scrapy.Request(url=next_url[0].attrib['href'], headers=headers, callback=self.parse_books, priority=1)
        else:
            first_url = response.selector.xpath("//a[@class='first']")
            yield scrapy.Request(url=first_url[0].attrib['href'], headers=headers, callback=self.parse_books, priority=1)

    def parse_chapters(self, response, **kwargs):
        book_name = response.selector.xpath("//meta[@property='og:novel:book_name']")[0].attrib['content'].strip()
        book_description = response.selector.xpath("//meta[@property='og:description']")[0].attrib['content'].strip()
        book_category = response.selector.xpath("//meta[@property='og:novel:category']")[0].attrib['content'].strip()
        book_author = response.selector.xpath("//meta[@property='og:novel:author']")[0].attrib['content'].strip()
        book_url = response.selector.xpath("//meta[@property='og:novel:read_url']")[0].attrib['content'].strip()
        old_book_info = {"book_url": book_url}
        old_chapter_urls = collection.distinct(key='chapter_url', filter=old_book_info)

        book_chapters = response.selector.xpath("//div[@id='list']/dl/dd/a")
        for book_chapter in book_chapters:
            chapter_url = 'https://www.xbiquge.la' + book_chapter.attrib['href']
            chapter_name = book_chapter.root.text.strip()
            # 已经被处理过得的请求不再继续处理，在此处获取所有url是为了减少mongo请求次数，避免filter压力过大
            if chapter_url in old_chapter_urls:
                self.logger.info("skip chapter url:%s, book name:%s, chapter name:%s", chapter_url, book_name, chapter_name)
                continue
            else:
                self.logger.info("crawl chapter url:%s, book name:%s, chapter name:%s", chapter_url, book_name, chapter_name)

            book_item = biquge_item(book_name=book_name, book_description=book_description, book_category=book_category,
                                    book_author=book_author, book_url=book_url, chapter_url=chapter_url,
                                    chapter_name=chapter_name)
            # 每隔20到30秒爬取下一章节内容
            # time.sleep(random.randint(15, 25))
            chapter_headers = {
                "Host": "www.xbiquge.la",
                "Connection": "keep-alive",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="92"',
                "sec-ch-ua-mobile": "?0",
                "Upgrade-Insecure-Requests": "Upgrade-Insecure-Requests",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Accept-Encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Referer": book_url
            }
            yield scrapy.Request(url=chapter_url, headers=chapter_headers, meta={"item": copy.deepcopy(book_item)},
                                 callback=self.parse_chapter, priority=3)

    def parse_chapter(self, response, **kwargs):
        chapter_contents = response.selector.xpath("//div[@id='content']/text()")
        lines = []
        for line in chapter_contents:
            if line.root != '\r':
                lines.append(line.root.strip())
        item = response.meta['item']
        item['chapter_content'] = lines
        item['timestamp'] = time.time()
        item['date_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        yield item
