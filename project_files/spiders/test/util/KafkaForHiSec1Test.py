import json
from json import JSONDecodeError

from kafka import KafkaConsumer
from loguru import logger

import logging.handlers

logger.add('test_hisec1.log', rotation="200 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

# servers = "localhost:9095"
servers = "192.168.50.27:9092"
# servers = "192.168.1.19:9092"
consumer = KafkaConsumer("logriver_siem", bootstrap_servers=servers, group_id="monitor1", auto_offset_reset="latest")

for msg in consumer:
    try:
        record_value = msg.value.decode('utf-8')
        if 'hisec' not in record_value:
            # logger.info(f"{msg.topic}:{msg.partition}:{msg.offset}: ignore not contains hisec")
            continue


        record_value_dic = json.loads(record_value)

        if ('appname' not in record_value_dic.keys()) or (record_value_dic['appname'] != 'hisec'):
            # logger.info(f"{msg.topic}:{msg.partition}:{msg.offset}: ignore")
            continue

        logger.info(f"{msg.topic}:{msg.partition}:{msg.offset}: "
                    f"key={'' if msg.key is None else msg.key.decode('utf-8')} "
                    f"value={record_value}")
    except (UnicodeDecodeError, JSONDecodeError):
        logger.error(f"{msg.topic}:{msg.partition}:{msg.offset}: "
                     f"key={msg.key} "
                     f"value={msg.value}")
