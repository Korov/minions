from kafka import KafkaAdminClient
from loguru import logger
from kafka.admin import ConfigResourceType, ConfigResource

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


def list_consumer_groups(bootstrap_servers="127.0.0.1:9092"):
    client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    try:
        consumers = client.list_consumer_groups()
        for consumer in consumers:
            logger.info(f"consumer:{consumer[0]}, type:{consumer[1]}")
    finally:
        client.close()


def list_consumer_group_offsets(bootstrap_servers="127.0.0.1:9092", group_ids=[]):
    client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    for group_id in group_ids:
        group_offset = client.list_consumer_group_offsets(group_id=group_id)
        logger.info(group_offset)


def describe_configs(bootstrap_servers="127.0.0.1:9092"):
    client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    cluster_infos = client.describe_cluster()
    broker_resources = []
    for cluster_info in cluster_infos["brokers"]:
        broker_id = cluster_info["node_id"]
        broker_resource = ConfigResource(resource_type=ConfigResourceType.BROKER, name=broker_id)
        broker_resources.append(broker_resource)
    configs = client.describe_configs(config_resources=broker_resources, include_synonyms=True)
    logger.info(f"broker configs:{configs}")

    topics = client.describe_topics()
    topic_resources = []
    for topic in topics:
        topic_name = topic.get('topic')
        topic_resource = ConfigResource(resource_type=ConfigResourceType.TOPIC, name=topic_name)
        topic_resources.append(topic_resource)

    configs = client.describe_configs(config_resources=topic_resources, include_synonyms=True)
    logger.info(f"topic configs:{configs}")