import threading
import time

import redis

from minions_spider import constant

redis_db0 = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=0, username=constant.REDIS_USER,
                        password=constant.REDIS_PASSWORD)


class connect_redis(threading.Thread):
    def __init__(self, redis_key, client_id):
        threading.Thread.__init__(self)
        self.redis_key = redis_key
        self.client_id = client_id

    def run(self):
        while True:
            time.sleep(8)
            key = "%s_%s" % (self.redis_key, self.client_id)
            print(key)
            redis_db0.set(name=key, value=time.time_ns(), ex=10)


all_keys = redis_db0.keys()
print(all_keys)
result = redis_db0.sadd("seen_urls_test", "demo")
print(result)
redis_db0.expire("seen_urls_test", 100)
result = redis_db0.smembers("seen_urls_test")
print(result)
count = redis_db0.scard("seen_urls_test")
print(count)

redis_db0.set("demo_key_1", time.time_ns(), ex=100)
redis_db0.set("demo_key_2", time.time_ns(), ex=100)
redis_db0.set("demo_key_3", time.time_ns(), ex=100)

redis_db0.sadd("set_key_test", "demo1", "demo2", "demo3")
values = redis_db0.sismember("set_key_test", "demo1")
print(values)
