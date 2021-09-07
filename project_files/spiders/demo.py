from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

url = 'https://www.xbiquge.la/0/82/8234452.html'
if not url.endswith('html'):
    print("not html")
else:
    print("html")

url = 'https://www.xbiquge.la/fenlei/3_2.html'
if 'fenlei' in url:
    print("aaa")

client = MongoClient('mongodb://spider:spider@korov.myqnapcloud.cn:27017/spider')
db = client['spider']
collection = db['seen_urls']

count = 0
for url in collection.find({}):
    count = count + 1
    print("url:%s, count:%s", url.get("chapter_url"), count)
