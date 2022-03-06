from kafka import KafkaAdminClient
from loguru import logger

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")


def describe_topics(bootstrap_servers="127.0.0.1:9092", topics=[]):
    """显示所有的topic详细信息"""
    if topics is None:
        topics = []
    topic_set = set(topics)

    client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    try:
        topics = client.describe_topics()
        for topic in topics:
            topic_name = topic.get('topic')

            if len(topic_set) > 0 and topic_name not in topic_set:
                continue

            logger.info(f"======topic:{topic_name}======")
            partitions = topic.get("partitions")
            for partition in partitions:
                logger.info(f"partition:{partition.get('partition')}, leader:{partition.get('leader')}, "
                            f"replicas:{partition.get('replicas')}, isr:{partition.get('isr')}, "
                            f"offline_replicas:{partition.get('offline_replicas')}")
    finally:
        client.close()
    return topics


def list_topics(bootstrap_servers="127.0.0.1:9092"):
    """显示所有的topic详细信息"""
    client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    try:
        topics = client.list_topics()
        logger.info(f"topics:{topics}")
    finally:
        client.close()
    return topics
