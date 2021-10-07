import random

from loguru import logger

from minions_spider.constant import PROXY_SET

logger.info(PROXY_SET)


proxy_list = list(PROXY_SET)
for index in range(0,10):
    i = random.randint(0, len(proxy_list) - 1)
    logger.info(i)
    proxy = proxy_list[i]
    logger.info(proxy)
