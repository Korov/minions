from kafka import KafkaAdminClient

from minions_spider.util import kafka_consumer as kafka_consumer, kafka_producer as kafka_producer, \
    kafka_admin as kafka_admin

servers = "192.168.205.135:30092"
# servers = "192.168.1.19:9092"
consumer = kafka_consumer.create_consumer(bootstrap_servers=servers, group_id="monitor")

# kafka_consumer.display_topic_consumers_count(consumer, ["alert_box"])
# kafka_consumer.display_authorized_topics(kafka_consumer=consumer)
# kafka_consumer.consumer_seek(consumer, "alert_box", 2, 0)
kafka_producer.send_msg(bootstrap_servers=servers, topic="alert_box", key="box_threat_data", msg="test")

# kafka_admin.list_topics(bootstrap_servers=servers)
kafka_admin.describe_topics(bootstrap_servers=servers, topics=[])
# kafka_admin.list_consumer_groups(bootstrap_servers=servers)
# kafka_admin.list_consumer_group_offsets(bootstrap_servers=servers, group_ids=["monitor"])
