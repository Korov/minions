import logging

from pymongo.errors import DuplicateKeyError
from scrapy.http import Request
from scrapy.dupefilters import BaseDupeFilter
from pymongo import MongoClient


class BiqugeFilter(BaseDupeFilter):
    def __init__(self):
        self.client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
        db = self.client['spider']
        self.book_collection = db['book_info']
        self.seen_urls_collection = db['seen_urls']
        self.logger = logging.getLogger(__name__)

    def request_seen(self, request: Request):
        request_chapter_url = request.url
        # 非html结尾的不过滤
        if (not request_chapter_url.endswith('html')) or ('fenlei' in request_chapter_url):
            self.logger.info("crawl url:%s with not chapter url", request_chapter_url)
            return False

        # 若url不在redis中，则要判断此url是否已经被处理完了，mongo中只存储被处理完的url
        old_book_info = {"chapter_url": request_chapter_url}
        seen_urls_count = self.seen_urls_collection.count_documents(old_book_info)
        if seen_urls_count > 0:
            return True

        book_count = self.book_collection.count_documents(old_book_info)

        if book_count > 0:
            try:
                # self.seen_urls_collection.insert_one(old_book_info)
                self.logger.info("filter chapter url:%s, seen urls count:%s, book count:%s", request_chapter_url,
                                 seen_urls_count, book_count)
            except DuplicateKeyError:
                self.logger.info("filter with duplicate chapter url:%s, seen urls count:%s, book count:%s",
                                 request_chapter_url, seen_urls_count, book_count)
            return True
        else:
            try:
                # self.seen_urls_collection.insert_one(old_book_info)
                self.logger.info("crawl chapter url:%s, seen urls count:%s, book count:%s", request_chapter_url,
                                 seen_urls_count, book_count)
                return False
            except DuplicateKeyError:
                self.logger.info("filter with duplicate chapter url:%s, seen urls count:%s, book count:%s",
                                 request_chapter_url, seen_urls_count, book_count)
                return True

    # can return a deferred
    def close(self, reason):
        self.client.close()

    # log that a request has been filtered
    def log(self, request: Request, spider):
        try:
            book_name = request.meta['item']['book_name']
            chapter_name = request.meta['item']['chapter_name']
        except Exception as e:
            self.logger.error('reason:%s', e)
            book_name = ''
            chapter_name = ''

        self.logger.info("url:%s, book_name:%s, chapter_name:%s has been filtered", request.url, book_name,
                         chapter_name)
