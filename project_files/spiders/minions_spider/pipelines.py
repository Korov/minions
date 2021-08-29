# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import redis


class biquge_pipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
        db = self.client['spider']
        self.collection = db['book_info']
        self.redis_db = redis.Redis(host='korov.myqnapcloud.cn', port=6379, db=0)
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        book_info = {"book_name": item['book_name'],
                     "book_description": item['book_description'],
                     "book_category": item['book_category'],
                     "book_author": item['book_author'],
                     "book_url": item['book_url'],
                     "chapter_url": item['chapter_url'],
                     "chapter_name": item['chapter_name'],
                     "chapter_content": item['chapter_content'],
                     "timestamp": item['timestamp'],
                     "date_time": item['date_time']}
        old_book_info = {"chapter_url": item['chapter_url']}
        count = self.collection.count_documents(old_book_info)
        if count == 0:
            try:
                self.collection.insert_one(book_info)
                # 处理完的url需要在redis中删除，确保redis中只存储正在处理中的url
                self.redis_db.srem('seen_urls', item['chapter_url'])
                self.logger.info("insert book:%s, chapter:%s", item['book_name'], item['chapter_name'])
            except DuplicateKeyError:
                self.logger.info("insert failed with book:%s, chapter:%s exists", item['book_name'], item['chapter_name'])
        else:
            self.logger.info("book:%s, chapter:%s exists", item['book_name'], item['chapter_name'])

        return item

    def close_spider(self, spider):
        self.client.close()
