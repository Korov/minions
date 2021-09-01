import redis

url = 'https://www.xbiquge.la/0/82/8234452.html'
if not url.endswith('html') :
    print("not html")
else:
    print("html")

url = 'https://www.xbiquge.la/fenlei/3_2.html'
if 'fenlei' in url:
    print("aaa")

redis_db = redis.Redis(host='korov.myqnapcloud.cn', port=6379, db=0)

result = redis_db.smembers("seen_urls")
print(result)