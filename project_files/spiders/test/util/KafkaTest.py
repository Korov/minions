from loguru import logger

from minions_spider.util import kafka_consumer as kConsumer, kafka_producer as kProducer, \
    kafka_admin as kAdmin

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

# servers = "localhost:9095"
servers = "korov.myqnapcloud.cn:9092"
consumer = kConsumer.create_consumer(bootstrap_servers=servers, group_id="monitor")

kConsumer.consumer_msg(topic="sink_log_river", bootstrap_servers=servers, group_id="monitor", auto_offset_reset="latest")
# kConsumer.display_topic_consumers_count(consumer, ["log_river_topic", "alert_topic"])
# kConsumer.display_authorized_topics(kafka_consumer=consumer)
# kConsumer.consumer_seek(consumer, "flink_siem", 4, 16573117)
# kProducer.send_msg(bootstrap_servers=servers, topic="tp1", key="key1", msg="test3")
#
# kAdmin.list_topics(bootstrap_servers=servers)
# kAdmin.describe_topics(bootstrap_servers=servers, topics=['log_river_topic', 'alert_topic', 'tp1', 'log_river', 'sink_topic'])
# kAdmin.list_consumer_groups(bootstrap_servers=servers)
# kAdmin.list_consumer_group_offsets(bootstrap_servers=servers, group_ids=["monitor"])

# kAdmin.describe_configs(bootstrap_servers=servers)
