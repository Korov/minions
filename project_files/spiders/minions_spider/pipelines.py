# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient


class biquge_pipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')

    def process_item(self, item, spider):
        db = self.client['spider_test']
        collection = db['book_info']
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
        collection.insert_one(book_info)
        return item

    def close_spider(self, spider):
        self.client.close()
