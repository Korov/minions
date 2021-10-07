import random

from loguru import logger

from minions_spider.constant import PROXY_SET

logger.info(PROXY_SET)


proxy_list = list(PROXY_SET)
for index in range(0,10):
    proxy = proxy_list[random.randint(0, len(proxy_list))]
    logger.info(proxy)
