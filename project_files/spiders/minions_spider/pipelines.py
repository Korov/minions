# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from pymongo import MongoClient


class biquge_pipeline(object):
    def open_spider(self, spider):
        self.f = open('biquge.log', 'w', encoding='utf-8')
        self.client = MongoClient('mongodb://admin:mongo@linux.korov.org:27017')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False))
        self.f.write('\n')
        db = self.client['spider']
        collection = db['book_info']
        book_info = {"book_url": item['book_url'],
                     "book_name": item['book_name'],
                     "author_name": item['author_name']}
        collection.insert_one(book_info)
        return item

    def close_spider(self, spider):
        self.f.close()
        self.client.close()
