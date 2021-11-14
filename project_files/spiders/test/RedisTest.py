import random

import redis
from loguru import logger

from minions_spider import constant

db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1, username=constant.REDIS_USER,
                 password=constant.REDIS_PASSWORD)

count = db.zcard("proxies:biquge")
# cursor, proxies = db.zscan("proxies:biquge", count=count)

# logger.info(proxies)

proxies = db.zrangebyscore("proxies:biquge", min=90, max=100, num=10, start=0, withscores=True)

logger.info(f"count:{len(proxies)}, random:{proxies[random.randint(0, len(proxies) - 1)][0].decode('utf8')} value:{proxies}")
