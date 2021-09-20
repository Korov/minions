# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

import redis
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from minions_spider import constant


class BiqugePipeline(object):
    def open_spider(self, spider):
        self.mongo_client = MongoClient(constant.MONGO_URL)
        mongo_db = self.mongo_client['spider']
        self.mongo_collection = mongo_db['book_info']
        self.redis_db0 = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=0,
                                     username=constant.REDIS_USER,
                                     password=constant.REDIS_PASSWORD)
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
        chapter_url = item["chapter_url"]
        old_book_info = {"chapter_url": chapter_url}
        count = self.mongo_collection.count_documents(old_book_info)
        if count == 0:
            try:
                self.mongo_collection.insert_one(book_info)
                self.logger.info("insert book:%s, chapter:%s", item['book_name'], item['chapter_name'])
            except DuplicateKeyError:
                self.logger.info("insert failed with book:%s, chapter:%s exists", item['book_name'],
                                 item['chapter_name'])
        else:
            self.logger.info("book:%s, chapter:%s exists", item['book_name'], item['chapter_name'])

        self.redis_db0.srem(spider.redis_value_key, chapter_url)
        self.logger.info(f"remove key:{spider.redis_value_key}, chapter url:{chapter_url}")
        return item

    def close_spider(self, spider):
        self.mongo_client.close()
