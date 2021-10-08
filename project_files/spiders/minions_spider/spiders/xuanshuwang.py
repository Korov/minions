import copy
import datetime
import time
import redis

import scrapy
from loguru import logger
from pymongo.mongo_client import MongoClient

from minions_spider import constant
from minions_spider.items import BiqugeItem
from minions_spider.util.RedisUtil import get_random_proxy

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": 'max-age=0',
    "Connection": "keep-alive",
    # "Cookie": "obj=1; clickbids=39094",
    "Host": "www.xuanshu.com",
    "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

mongo_client = MongoClient(constant.MONGO_URL)
mongo_db_spider = mongo_client['spider']
book_collection = mongo_db_spider['xuanshu_info']
proxy_db = None


class xuanshu(scrapy.Spider):
    name = "xuanshu"
    allowed_domains = ['xuanshu.com']
    custom_settings = {
        'ITEM_PIPELINES': {'minions_spider.pipelines.XuanshuPipeline': 300},
        # 'DOWNLOADER_MIDDLEWARES': {'minions_spider.middlewares.MinionsSpiderDownloaderMiddleware': 300},
        'CONCURRENT_REQUESTS': 32,
        'DOWNLOAD_TIMEOUT': 20,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 50,
        'DOWNLOAD_DELAY': 1,
        'COOKIES_ENABLED': True
    }

    def start_requests(self):
        proxy_db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1, username=constant.REDIS_USER,
                         password=constant.REDIS_PASSWORD)
        urls = [
            "https://www.xuanshu.com/sort1/1.html",
        ]
        for url in urls:
            headers["Referer"] = url
            proxy = get_random_proxy()
            yield scrapy.Request(url=url, headers=headers,
                                 meta={'proxy': f'https://{proxy}'},
                                 callback=self.parse_books, priority=1)

    def parse_books(self, response, **kwargs):
        books = response.selector.xpath("//div[@class='xname']/a")
        # for book in books:
        #     book_url = f"https://www.xuanshu.com{str(book.attrib['href'])}"
        #     headers.pop("Referer")
        #     yield scrapy.Request(url=book_url, headers=headers, callback=self.parse_chapters, priority=2)
        book_url = f"https://www.xuanshu.com{str(books[0].attrib['href'])}"
        headers.pop("Referer")
        proxy = get_random_proxy()
        yield scrapy.Request(url=book_url, headers=headers,
                             meta={'proxy': f'https://{proxy}'},
                             callback=self.parse_chapters, priority=2)

    def parse_chapters(self, response, **kwargs):
        chapters = response.selector.xpath("//div[@class='pc_list']/ul/li/a")
        book_id = str.split(response.url, '/')[4]
        book_category = response.selector.xpath("//dd/a/text()")[1].extract()
        book_name = response.selector.xpath("//h1/text()").extract()[0]
        author_name = str.split(response.selector.xpath("//dl/text()")[0].extract(), "：")[1]
        book_desc = response.selector.xpath("//div[@class='info_des']//text()")[20].extract().strip()
        for chapter in chapters:
            chapter_url = f"https://www.xuanshu.com/book/{book_id}/{str(chapter.attrib['href'])}"
            chapter_name = str(chapter.xpath("text()").extract()[0])

            book_item = BiqugeItem(book_name=book_name, book_description=book_desc, book_category=book_category,
                                   book_author=author_name, book_url=f"https://www.xuanshu.com/book/{book_id}",
                                   chapter_url=chapter_url,
                                   chapter_name=chapter_name)
            proxy = get_random_proxy()
            yield scrapy.Request(url=chapter_url, headers=headers, meta={"item": copy.deepcopy(book_item),
                                                                         'proxy': f'https://{proxy}'},
                                 callback=self.parse_chapter, priority=3)

    def parse_chapter(self, response, **kwargs):
        chapter_contents = response.selector.xpath("//div[@id='content1']/text()")
        lines = []
        for line in chapter_contents:
            if line.root != '\r':
                lines.append(line.root.strip())
        item = response.meta['item']
        item['chapter_content'] = lines
        item['timestamp'] = time.time()
        item['date_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logger.info(f"book_name:{item['book_name']}, chapter_name:{item['chapter_name']}")
        yield item
