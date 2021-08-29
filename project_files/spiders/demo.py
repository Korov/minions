import redis

url = 'https://www.xbiquge.la/0/82/8234452.html'
if not url.endswith('html') :
    print("not html")
else:
    print("html")

redis_db = redis.Redis(host='korov.myqnapcloud.cn', port=6379, db=0)
redis_db.delete("seen_urls")

result = redis_db.smembers("seen_urls")
print(result)