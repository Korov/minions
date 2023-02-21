import json

from kafka import KafkaConsumer
from loguru import logger

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

# servers = "localhost:9095"
servers = "192.168.50.27:9092"
# servers = "192.168.1.19:9092"
consumer = KafkaConsumer("logriver_siem", bootstrap_servers=servers, group_id="monitor1", auto_offset_reset="earliest")

for msg in consumer:
    try:
        record_value = msg.value.decode('utf-8')
        record_value_dic = json.loads(record_value)
        if record_value_dic['appname'] != 'hisec':
            continue

        logger.info(f"{msg.topic}:{msg.partition}:{msg.offset}: "
                    f"key={'' if msg.key is None else msg.key.decode('utf-8')} "
                    f"value={record_value}")
    except UnicodeDecodeError:
        logger.error(f"{msg.topic}:{msg.partition}:{msg.offset}: "
                     f"key={msg.key} "
                     f"value={msg.value}")
