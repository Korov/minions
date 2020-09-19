from kafka import KafkaConsumer
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
consumer = KafkaConsumer('heros', bootstrap_servers=settings.get('BOOTSTRAP_SERVERS'))


def consumer_msg(topic, server):
    if (not topic is None) and (not server is None):
        consumer = KafkaConsumer(topic, bootstrap_servers=server)

    index = 0
    for msg in consumer:
        index = index + 1
        print(index)
        print(msg)
