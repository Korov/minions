from kafka import KafkaAdminClient
from kafka.admin import ConfigResourceType, ConfigResource
from loguru import logger

from minions_spider.util import kafka_consumer as kafka_consumer, kafka_producer as kafka_producer, \
    kafka_admin as kafka_admin

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

# servers = "localhost:9092"
servers = "192.168.205.135:30092"
consumer = kafka_consumer.create_consumer(bootstrap_servers=servers, group_id="monitor")

kafka_consumer.consumer_msg(topic="flink_siem", bootstrap_servers=servers, group_id="monitor",
                            auto_offset_reset="latest")
# kafka_consumer.display_topic_consumers_count(consumer, ["flink_siem"])
# kafka_consumer.display_authorized_topics(kafka_consumer=consumer)
# kafka_consumer.consumer_seek(consumer, "flink_siem", 4, 16573117)
# kafka_producer.send_msg(bootstrap_servers=servers, topic="alert_box", key="box_threat_data", msg="test")

# kafka_admin.list_topics(bootstrap_servers=servers)
# kafka_admin.describe_topics(bootstrap_servers=servers, topics=[])
# kafka_admin.list_consumer_groups(bootstrap_servers=servers)
# kafka_admin.list_consumer_group_offsets(bootstrap_servers=servers, group_ids=["monitor"])

# kafka_admin.describe_configs(bootstrap_servers=servers)
