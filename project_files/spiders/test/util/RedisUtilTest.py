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
# logger.info(redis_server.keys(pattern="*"))
# for key in redis_server.scan_iter(match="*"):
#     logger.info(f"key:{key.decode('utf-8')}, value:{redis_server.get(key).decode('utf-8')}")
# logger.info(redis_server.scan(cursor=0, match="*"))

# 实现事务
# with redis_server.pipeline() as pipe:
#     # 监视一个key，如果在执行期间被修改了，抛出WatchError
#     pipe.watch("key_1")
#     pipe.multi()
#     pipe.set("key_1", "value1")
#     pipe.set("key_2", "value2")
#     pipe.execute()

redis_server.publish(channel="channel1", message="message1")

redis_subscribe = redis_server.pubsub()
redis_subscribe.subscribe("channel1")
for item in redis_subscribe.listen():
    logger.info(item)
