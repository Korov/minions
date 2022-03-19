import redis
from loguru import logger

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")

redis_server = redis.StrictRedis(host='localhost', port=6379, db=0, password="redis")

# logger.info(redis_server.keys(pattern="*"))
# logger.info(redis_server.set(name="demo_key", value="demo_value", nx=True))
# logger.info(redis_server.keys(pattern="*"))
# logger.info(redis_server.get(name="demo_key").decode("utf-8"))
# for i in range(1,100):
#     logger.info(redis_server.set(name=i, value=i, nx=True))
logger.info(redis_server.keys(pattern="*"))
for value in redis_server.scan_iter(match="*"):
    logger.info(redis_server.get(value))
logger.info(redis_server.scan(cursor=0,match="*"))
