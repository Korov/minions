import random
import redis
from loguru import logger

from minions_spider import constant


def get_random_proxy():
    # proxy_db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1, username=constant.REDIS_USER,
    #                        password=constant.REDIS_PASSWORD)
    # ips = proxy_db.zrange("proxies:universal", 0, 100)
    ips = ['103.134.30.137:8080']
    random_index = random.randint(0, len(ips) - 1)
    random_ip = ips[random_index]
    # proxy_db.close()
    # return random_ip.decode()
    logger.info(f"get proxy:{random_ip}")
    return random_ip
