from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

url = 'https://www.xbiquge.la/0/82/8234452.html'
if not url.endswith('html') :
    print("not html")
else:
    print("html")

url = 'https://www.xbiquge.la/fenlei/3_2.html'
if 'fenlei' in url:
    print("aaa")

client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
db = client['spider']
collection = db['seen_urls']
old_book_info = {"chapter_url": 'chapter_url'}
count = collection.delete_one(old_book_info)
print(count)
try:
    count = collection.insert_one(old_book_info)
except DuplicateKeyError:
    count = 0
print(count)
old_info = collection.find_one(old_book_info)
print(old_info)
try:
    count = collection.insert_one(old_book_info)
except DuplicateKeyError:
    count = 0
print(count)



