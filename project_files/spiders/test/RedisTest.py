import redis

from minions_spider import constant

redis_db0 = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=0, username=constant.REDIS_USER,
                        password=constant.REDIS_PASSWORD)

all_keys = redis_db0.keys()
print(all_keys)
result = redis_db0.sadd("seen_urls_test", "demo")
print(result)
result = redis_db0.smembers("seen_urls_test")
print(result)
count = redis_db0.scard("seen_urls_test")
print(count)
