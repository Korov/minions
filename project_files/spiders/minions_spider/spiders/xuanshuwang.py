import logging

import scrapy
from pymongo.mongo_client import MongoClient

from minions_spider import constant

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": 'max-age=0',
    "Connection": "keep-alive",
    "Cookie": "obj=1; clickbids=39094",
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
logger = logging.getLogger(__name__)


class xuanshu(scrapy.Spider):
    name = "xuanshu"
    allowed_domains = ['xuanshu.com']
    custom_settings = {
        # 'DOWNLOADER_MIDDLEWARES': {'minions_spider.middlewares.biquge_middleware': 300},
        'DOWNLOAD_TIMEOUT': 120,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 50,
        # 'CONCURRENT_REQUESTS_PER_IP': 50,
        'DOWNLOAD_DELAY': 5,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,
        'AUTOTHROTTLE_MAX_DELAY': 60,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 10.0
    }

    def start_requests(self):
        urls = [
            "https://www.xuanshu.com/sort1/1.html",
        ]
        for url in urls:
            headers["Referer"] = url
            yield scrapy.Request(url=url, headers=headers, callback=self.parse_books, priority=1)

    def parse_books(self, response, **kwargs):
        books = response.selector.xpath("//div[@class='xupl']/a")
        logger.info(books)
