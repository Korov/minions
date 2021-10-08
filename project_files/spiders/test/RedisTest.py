import random

import redis
from loguru import logger

from minions_spider import constant

db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1, username=constant.REDIS_USER,
                 password=constant.REDIS_PASSWORD)

count = db.zcard("proxies:universal")

logger.info(count)
ips = db.zrange("proxies:universal", 0, 100)
logger.info(ips)
random_index = random.randint(0, len(ips) - 1)
random_ip = ips[random_index]
logger.info(random_ip.decode())
