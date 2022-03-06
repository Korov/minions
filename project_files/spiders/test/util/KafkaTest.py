import minions_spider.util.kafka_consumer as kafka_consumer

consumer = kafka_consumer.create_consumer(bootstrap_servers="192.168.205.135:30092", group_id="monitor")
kafka_consumer.display_all_topics(consumer)
kafka_consumer.display_topic_consumers(consumer, ["alert_box", "raw_message"])
kafka_consumer.display_topic_partition(consumer, ["raw_message"])
kafka_consumer.display_topic_consumers(consumer, ["raw_message"])
kafka_consumer.consumer_seek(consumer, "raw_message", 0, 1269806324)
