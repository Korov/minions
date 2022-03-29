import time
import uuid

from loguru import logger

#
# location = '/home/korov/Desktop/gitrepo/minions/project_files/spiders/fake_useragent.json'
# logger.info(location)
# ua = UserAgent(use_cache_server=False, verify_ssl=False)
#
# logger.info(ua.random)

id = uuid.uuid4().__str__()
logger.info(id.__str__())
id = uuid.uuid4()
logger.info(id.__str__())
logger.info(time.time())
