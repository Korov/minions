from loguru import logger
from kazoo.client import KazooClient, KazooState

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")

zk = KazooClient(hosts='localhost:2181', timeout=10.0)

zk.start()
data, stat = zk.get('/')
logger.info(data.decode("utf-8"))
logger.info(stat)

children = zk.get_children("/")
logger.info(children)

zk.stop()
zk.close()
