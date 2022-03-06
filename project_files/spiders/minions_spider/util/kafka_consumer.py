from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from loguru import logger

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")


def consumer_msg(topic, bootstrap_servers, group_id="default_group", auto_offset_reset="earliest"):
    if (not topic is None) and (not bootstrap_servers is None):
        consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, group_id=group_id,
                                 auto_offset_reset=auto_offset_reset)
    for msg in consumer:
        logger.info(
            f"{msg.topic}:{msg.partition}:{msg.offset}: key={msg.key.decode('utf-8')} value={msg.value.decode('utf-8')}")


def create_consumer(bootstrap_servers="127.0.0.1:9092", group_id="default_group"):
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id=group_id)
    logger.info(f"create kafka consumer:{bootstrap_servers}, group id:{group_id}")
    return consumer


def display_all_topics(kafka_consumer=None):
    topics = kafka_consumer.topics()
    logger.info("====all topics====")
    for topic in topics:
        logger.info(f"topic name:{topic}")
    return topics


def display_topic_partition(kafka_consumer=None, topics=[]):
    for topic in topics:
        partitions = kafka_consumer.partitions_for_topic(topic)
        logger.info(f"====topic:{topic}, partitions:====")
        topic_partitions = []
        for partition in partitions:
            topic_partitions.append(TopicPartition(topic=topic, partition=partition))

        kafka_consumer.assign(topic_partitions)
        beginning_offsets = kafka_consumer.beginning_offsets(topic_partitions)

        for topic_partition in topic_partitions:
            position = kafka_consumer.position(topic_partition)
            logger.info(
                f"topic:{topic_partition.topic}, partition:{topic_partition.partition}, beginning offsets:{beginning_offsets[topic_partition]}, end position:{position}, valid count:{position - beginning_offsets[topic_partition]}")


def display_topic_consumers(kafka_consumer=None, topics=[]):
    for topic in topics:
        partitions = kafka_consumer.partitions_for_topic(topic)
        logger.info(f"====topic:{topic}, partitions:====")
        topic_partitions = []
        for partition in partitions:
            topic_partitions.append(TopicPartition(topic=topic, partition=partition))

        kafka_consumer.assign(topic_partitions)
        beginning_offsets = kafka_consumer.beginning_offsets(topic_partitions)

        for topic_partition in topic_partitions:
            position = kafka_consumer.position(topic_partition)
            logger.info(
                f"topic:{topic_partition.topic}, partition:{topic_partition.partition}, beginning offsets:{beginning_offsets[topic_partition]}, position:{position}, valid count:{position - beginning_offsets[topic_partition]}")


def consumer_seek(kafka_consumer=None, topic=None, partition=None, offset=0):
    topic_partition = TopicPartition(topic=topic, partition=partition, )
    kafka_consumer.assign([topic_partition])
    kafka_consumer.seek(topic_partition, offset)
    for msg in kafka_consumer:
        message_key = msg.key
        if message_key is None:
            logger.info(
                f"{msg.topic}:{msg.partition}:{msg.offset}: value={msg.value.decode('utf-8')}")
        else:
            logger.info(
                f"{msg.topic}:{msg.partition}:{msg.offset}: key={msg.key.decode('utf-8')} value={msg.value.decode('utf-8')}")
