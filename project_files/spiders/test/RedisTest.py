import random

import redis
from loguru import logger

from minions_spider import constant

db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1, username=constant.REDIS_USER,
                 password=constant.REDIS_PASSWORD)

count = db.zcard("proxies:biquge")
cursor, proxies = db.zscan("proxies:biquge", count=count)

logger.info(proxies)
