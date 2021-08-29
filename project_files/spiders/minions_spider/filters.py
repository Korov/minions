import logging
from scrapy.http import Request
from scrapy.dupefilters import BaseDupeFilter
from pymongo import MongoClient
import redis


class BiqugeFilter(BaseDupeFilter):
    def __init__(self):
        self.client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
        db = self.client['spider']
        self.collection = db['book_info']
        self.redis_db = redis.Redis(host='korov.myqnapcloud.cn', port=6379, db=0)
        self.logger = logging.getLogger(__name__)

    def request_seen(self, request: Request):
        old_chapter_url = request.url
        # redis中只存储正在处理中的url，若存在则说明此url正在被别的爬虫爬取中
        is_members = self.redis_db.sismember('seen_urls', old_chapter_url)
        if is_members:
            return True


        old_book_info = {"chapter_url": old_chapter_url}
        count = self.collection.count_documents(old_book_info)
        if count > 0:
            return True
        else:
            self.redis_db.set("seen_urls", request.url)
            return False

    # can return a deferred
    def close(self, reason):
        self.client.close()

    # log that a request has been filtered
    def log(self, request: Request, spider):
        try:
            book_name = request.meta['item']['book_name']
            chapter_name = request.meta['item']['chapter_name']
        except Exception as e:
            logging.error('reason:', e)
            book_name = ''
            chapter_name = ''
        self.logger.info("url:%s, book_name:%s, chapter_name:%s has been filtered", request.url, book_name,
                         chapter_name)
