import random

from loguru import logger

#
# location = '/home/korov/Desktop/gitrepo/minions/project_files/spiders/fake_useragent.json'
# logger.info(location)
# ua = UserAgent(use_cache_server=False, verify_ssl=False)
#
# logger.info(ua.random)
value = "aa'ff'afe"
ids = set()
while len(ids) < 500:
    ids.add(str(random.randrange(0, 10000000)))
logger.info("('" + str.join("', '", ids) + "')")


logger.info(where_id)
