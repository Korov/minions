from loguru import logger
from kazoo.client import KazooClient, KazooState

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")

zk = KazooClient(hosts='192.168.50.115:2181')
# zk = KazooClient(hosts='localhost:2181')

zk.start()
data, stat = zk.get('/')
logger.info(data.decode("utf-8"))
logger.info(stat)

# children = zk.get_children("/cn/yottabyte/yotta_siem")
# logger.info(children)

# actionCode = zk.delete(path="/cn/yottabyte/yotta_siem/leader")
# logger.info(actionCode)
#
# children = zk.get_children("/cn/yottabyte/yotta_siem")
# logger.info(children)

zk.stop()
zk.close()
