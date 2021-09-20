import copy
import datetime
import logging
import threading
import time
import uuid

import redis
import scrapy
from pymongo.mongo_client import MongoClient

from minions_spider import constant
from minions_spider.items import BiqugeItem

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

mongo_client = MongoClient(constant.MONGO_URL)
mongo_db_spider = mongo_client['spider']
book_collection = mongo_db_spider['book_info']
seen_urls_collection = mongo_db_spider["seen_urls"]
redis_db0 = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=0, username=constant.REDIS_USER,
                        password=constant.REDIS_PASSWORD)


class connect_redis(threading.Thread):
    def __init__(self, redis_key):
        threading.Thread.__init__(self)
        self.redis_key = redis_key
        self.daemon = True
        self.logger = logging.getLogger(__name__)

    def run(self):
        while True:
            time.sleep(10)
            redis_db0.set(name=self.redis_key, value=time.time_ns(), ex=20)

            client_uuids = set()
            value_keys = redis_db0.keys("spider_biquge_value_*")
            self.logger.info(f"all value keys:{value_keys}")
            for key in value_keys:
                key_str = key.decode("utf8")
                client_uuids.add(key_str.replace("spider_biquge_value_", ""))

            client_ids = redis_db0.keys("spider_biquge_client_id_*")
            self.logger.info(f"all client ids:{client_ids}")
            for key in client_ids:
                client_id = key.decode("utf8")
                client_uuid = client_id.replace("spider_biquge_client_id_", "")
                if client_uuid in client_uuids:
                    delete_key = client_uuids.remove(client_uuid)
                    self.logger.info(f"deleted key:{delete_key}")
                else:
                    self.logger.info(f"client id:{client_uuid}, client ids:{client_uuids}")

            self.logger.info(f"delete client uuids:{client_uuids}")
            if len(client_uuids) > 0:
                for client_uuid in client_uuids:
                    set_key = f"spider_biquge_value_{client_uuid}"
                    delete_count = redis_db0.delete(set_key)
                    if delete_count == 1:
                        self.logger.info(f"delete set key:{set_key}")
                    else:
                        self.logger.info(f"key not exists:{set_key}")


class biquge(scrapy.Spider):
    client_id = uuid.uuid1()
    redis_client_key = f"spider_biquge_client_id_{client_id}"
    redis_value_key = f"spider_biquge_value_{client_id}"
    thread = connect_redis(redis_client_key)
    thread.start()

    name = "biquge"
    allowed_domains = ['xbiquge.la']
    custom_settings = {
        'ITEM_PIPELINES': {'minions_spider.pipelines.BiqugePipeline': 300},
        # 'DOWNLOADER_MIDDLEWARES': {'minions_spider.middlewares.biquge_middleware': 300},
        'DUPEFILTER_CLASS': 'minions_spider.filters.BiqugeFilter',
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
            yield scrapy.Request(url=first_url[0].attrib['href'], headers=headers, callback=self.parse_books,
                                 priority=1)

    def parse_chapters(self, response, **kwargs):
        book_name = response.selector.xpath("//meta[@property='og:novel:book_name']")[0].attrib['content'].strip()
        book_description = response.selector.xpath("//meta[@property='og:description']")[0].attrib['content'].strip()
        book_category = response.selector.xpath("//meta[@property='og:novel:category']")[0].attrib['content'].strip()
        book_author = response.selector.xpath("//meta[@property='og:novel:author']")[0].attrib['content'].strip()
        book_url = response.selector.xpath("//meta[@property='og:novel:read_url']")[0].attrib['content'].strip()
        old_book_info = {"book_url": book_url}
        old_chapter_urls = book_collection.distinct(key='chapter_url', filter=old_book_info)

        book_chapters = response.selector.xpath("//div[@id='list']/dl/dd/a")
        for book_chapter in book_chapters:
            chapter_url = 'https://www.xbiquge.la' + book_chapter.attrib['href']
            chapter_name = book_chapter.root.text.strip()
            # 已经被处理过得的请求不再继续处理，在此处获取所有url是为了减少mongo请求次数，避免filter压力过大
            if chapter_url not in old_chapter_urls:

                client_uuids = set()
                value_keys = redis_db0.keys("spider_biquge_value_*")
                self.logger.info(f"all value keys:{value_keys}")
                for key in value_keys:
                    key_str = key.decode("utf8")
                    client_uuids.add(key_str.replace("spider_biquge_value_", ""))

                for client_uuid in client_uuids:
                    if redis_db0.sismember(f"spider_biquge_value_{client_uuid}", chapter_url):
                        self.logger.info(f"chapter url:{chapter_url} has been handled by client id:{client_uuid}")
                        continue

                insert_count = redis_db0.sadd(self.redis_value_key, chapter_url)
                if insert_count == 1:
                    self.logger.info("crawl chapter url:%s, book name:%s, chapter name:%s", chapter_url, book_name,
                                     chapter_name)
                else:
                    self.logger.info("skip chapter url:%s, book name:%s, chapter name:%s", chapter_url, book_name,
                                     chapter_name)
                    continue

            book_item = BiqugeItem(book_name=book_name, book_description=book_description, book_category=book_category,
                                   book_author=book_author, book_url=book_url, chapter_url=chapter_url,
                                   chapter_name=chapter_name)
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
