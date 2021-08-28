import logging
from scrapy.http import Request
from scrapy.dupefilters import BaseDupeFilter
from pymongo import MongoClient


class BiqugeFilter(BaseDupeFilter):
    def __init__(self):
        self.client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
        db = self.client['spider']
        self.collection = db['book_info']
        self.logger = logging.getLogger(__name__)

    def request_seen(self, request: Request):
        old_book_info = {"chapter_url": request.url}
        count = self.collection.count_documents(old_book_info)
        if count > 0:
            return True
        else:
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
