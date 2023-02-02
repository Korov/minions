from loguru import logger

from minions_spider.util import kafka_consumer as kConsumer, kafka_producer as kProducer, \
    kafka_admin as kAdmin

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

servers = "localhost:9095"
# servers = "192.168.50.100:9092"
consumer = kConsumer.create_consumer(bootstrap_servers=servers, group_id="monitor")

kConsumer.consumer_msg(topic="t2", bootstrap_servers=servers, group_id="monitor", auto_offset_reset="latest")
# kConsumer.display_topic_consumers_count(consumer, ["kafka_topic", "kafka_log_river"])
# kConsumer.display_authorized_topics(kafka_consumer=consumer)
# kConsumer.consumer_seek(consumer, "sink_log_river", 0, 1)
# kProducer.send_msg(bootstrap_servers=servers, topic="flink_siem", key="flink_alert", msg='{"__att_ck__":"{\\"TA0040\\":{\\"T1485\\":[]}}","__meta__":{"rule_id":"360a3f0c98c94e4daa8029f0c80fe50d","start_time":1671100353000,"rule":"","window_size_ms":120000,"uuid":"cd15e3c9dee348b1becaba1a6d068d2f","timestamp":1671100353000},"threat_level":0,"net_flow":1,"rule_name":"IDS规则测试_5885","extend_threat_classif":"","__create_case__":1,"threat_classif":"","threat_state":0,"dst_ip":"2409:8038:2000:206a:0:0:0:1","disposal":"百度地址: https://www.baidu.com","src_ip":"2409:8a38:7819:8290:c882:4b4f:de37:7553","src_port":[64548],"count_":1,"__inner_alert__":0,"__issue_merge_open__":0,"__inner_event__":0,"threat_type":0,"threat_stage":0,"pipeline_ids":["wafdad0a9f3-4b11-467e-ad0a-ca6ea171f6cf","IPc657e5f8-f111-4feb-ab8f-20c0a4dac72c","waf36a1196a-8690-4e37-9380-f48eb57ca70b"],"desc":"自动化数据"}')
#
# kAdmin.list_topics(bootstrap_servers=servers)
# kAdmin.describe_topics(bootstrap_servers=servers, topics=['alert_topic'])
# kAdmin.list_consumer_groups(bootstrap_servers=servers)
# kAdmin.list_consumer_group_offsets(bootstrap_servers=servers, group_ids=["monitor"])

# kAdmin.describe_configs(bootstrap_servers=servers)
