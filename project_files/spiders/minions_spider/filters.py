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
        # 非html结尾的不过滤
        if not old_chapter_url.endswith('html'):
            return False

        # redis中只存储正在处理中的url，若存在则说明此url正在被别的爬虫爬取中
        is_members = self.redis_db.sismember('seen_urls', old_chapter_url)

        # 若url不在redis中，则要判断此url是否已经被处理完了，mongo中只存储被处理完的url
        old_book_info = {"chapter_url": old_chapter_url}
        count = self.collection.count_documents(old_book_info)

        if count > 0:
            if is_members:
                # 如果url即在mongo中存在又在redis中存在，需要将redis中的数据删除，确保redis中只保存正在处理中的url
                self.redis_db.srem('seen_urls', old_chapter_url)
            return True
        else:
            if is_members:
                # 如果url在mongo中不存在，但是在redis中存在，则表明url正在被别的爬虫处理，此爬虫不再处理此url
                return True
            else:
                # url在mongo中不存在，在redis中不存在，则表明url还未被处理，此爬虫开始处理此url
                add_count = self.redis_db.sadd("seen_urls", old_chapter_url)
                # add_count为1说明插入成功，此url被此spider获取，否则，此url被别的spider抢走了则此spider不再处理此url
                if add_count == 1:
                    return False
                else:
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
