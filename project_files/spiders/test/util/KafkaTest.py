from kafka import KafkaAdminClient

from minions_spider.util import kafka_consumer as kafka_consumer, kafka_producer as kafka_producer

servers = "192.168.205.135:30092"
consumer = kafka_consumer.create_consumer(bootstrap_servers=servers, group_id="monitor")

# kafka_consumer.display_all_topics(bootstrap_servers=servers)
# kafka_consumer.display_topic_partition(consumer, ["alert_box"])
# kafka_consumer.display_topic_consumers_count(consumer, ["alert_box"])
# kafka_consumer.display_topic_consumers(bootstrap_servers=servers, topics=["alert_box"])
# kafka_consumer.display_topic_consumers(consumer, ["raw_message"])
# kafka_consumer.consumer_seek(consumer, "alert_box", 2, 0)
# kafka_producer.send_msg(bootstrap_servers=servers, topic="alert_box", key="box_threat_data", msg="test")

client = KafkaAdminClient(bootstrap_servers=servers)
topics = client.describe_topics()
print(f"topics:{topics}")
# for topic in topics:
#     print(f"topics:{topic}\n")
