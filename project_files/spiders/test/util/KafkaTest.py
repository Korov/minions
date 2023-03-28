from loguru import logger

from minions_spider.util import kafka_consumer as kConsumer, kafka_producer as kProducer, \
    kafka_admin as kAdmin

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

# servers = "localhost:9095"
servers = "192.168.50.27:9092"
# servers = "192.168.1.19:9092"
consumer = kConsumer.create_consumer(bootstrap_servers=servers, group_id="monitor")

# kConsumer.consumer_msg(topic="logriver_siem", bootstrap_servers=servers, group_id="monitor_1", auto_offset_reset="earliest")
# kConsumer.display_topic_consumers_count(consumer, ["kafka_topic", "kafka_log_river"])
# kConsumer.display_authorized_topics(kafka_consumer=consumer)
# kConsumer.consumer_seek(consumer, "sink_log_river", 0, 1)
# kProducer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg='{"logtype":"hisec","appname":"hisec","event_name":"Information Disclosure Attack","tag":["hisec"],"id":"50284a22e0b84c5f9ffc1dbd5e0f323c","hisec":{"AttackerHostUniqueID":"00:87:36:08:a4:11","OnThreatRegionPath":"-1","EventType":"12000","DestPort":"80","OriginalData":"aHR0cF91cmk6L3htbC9leGFtcGxlMS5waHA/eG1sPTw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IlVURi04Ij8+PCFET0NUWVBFIGZvbyBbDQo8IUVMRU1FTlQgZm9vIEFOWSA+PCFFTlRJVFkgJSB4eGUgU1lTVEVNICJodHRwOi8vaGl0ODF6TFFGb2U3cS5ieHNzLm1lLyI+Ow==","AttackStatus":"2","OnThreatAssetTypeId":"5","AttackerIP":"192.168.2.101","ThreatEventStatus":"1","DstHostUniqueID":"192.168.2.39","TenantID":"00000000-0000-0000-0000-000000000000","ReceiveDate":"2023-02-27T09:35:12.417","RegionName":"系统租户","AttackPhase":"16","EventSrcType":"Flowprobe","RegionID":"global","DstRegionID":"-1","OnThreatIP":"192.168.2.39","AttackEvidenceID":"00000400000006300000000063fc7821","SrcPort":"13566","OriEventID":"f1da1f94-52d8-44c1-a33e-c6632cf10c6e","TenantName":"系统租户","DestIP":"192.168.2.39","RuleID":"99c56153-1369-4a6e-a29d-528835c15a05","SrcIP":"192.168.2.101","SrcRegionPath":"-1","ForensicsData":"R0VUIC94bWwvZXhhbXBsZTEucGhwP3htbD08JTNmeG1sJTIwdmVyc2lvbiUzZCUyMjEuMCUyMiUyMGVuY29kaW5nJTNkJTIyVVRGLTglMjIlM2Y+JTBkJTBhPCUyMURPQ1RZUEUlMjBmb28lMjAlNWIlMGQlMGE8JTIxRUxFTUVOVCUyMGZvbyUyMEFOWSUyMD4lMGQlMGE8JTIxRU5USVRZJTIwJTI1JTIweHhlJTIwU1lTVEVNJTIwJTIyaHR0cDovL2hpdDgxekxRRm9lN3EuYnhzcy5tZS8lMjI+JTBkJTBhJTI1eHhlOyUwZCUwYSU1ZD4lMGQlMGEgSFRUUC8xLjENCkhvc3Q6IDE5Mi4xNjguMi4zOQ0KQ29ubmVjdGlvbjogS2VlcC1hbGl2ZQ0KQWNjZXB0LUVuY29kaW5nOiBnemlwLGRlZmxhdGUNClVzZXItQWdlbnQ6IE1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4yMSAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS80MS4wLjIyMjguMCBTYWZhcmkvNTM3LjIxDQpBY2NlcHQ6ICovKg0KDQo=","AppProtocol":"HTTP","EventID":"b71905b1-3e94-40e4-8bff-02feb45fc72d","ReceiveTime":"1677490512417","AggregationEventID":"918de17f-31d6-456f-8034-60229b99ca17","DstTenantID":"-1","EventLevel":"3","Action":"2","EventCategory":"2","DetectType":"1","EventSrcCategory":"HiSec Insight","RecentTime":"1677490511","AttackerRegionPath":"-1","URL":"http://192.168.2.39/xml/example1.php?xml=<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE foo [\r\n<!ELEMENT foo ANY ><!ENTITY % xxe SYSTEM \"http://hit81zLQFoe7q.bxss.me/\">","EventSubType":"12004","SignatureID":"2001109","ConfidenceLevel":"80","SrcHostUniqueID":"00:87:36:08:a4:11","DataType":"6","DstRegionPath":"-1","OriMetaDataID":"ee3163fc781c004001000000","Protocol":"TCP","EventDetailSrc":"Correlation Analysis","SrcTenantID":"-1","EventSrcIP":"10.1.0.10","OnThreatHost":"192.168.2.39","OS":"any","AtkDirection":"1","IsThreatDecision":"1","OccurTime":"1677490511","EventName":"Information Disclosure Attack","MergeCount":"1","ObjectName":"XML External Entity Attack - Remote Access Protocol","EventClass":"1514030","RegionPath":"1","SrcRegionID":"-1","SrcMac":"00:87:36:08:a4:11"},"timestamp":"1677490511000"}')
#
# kAdmin.list_topics(bootstrap_servers=servers)
# kAdmin.describe_topics(bootstrap_servers=servers, topics=['alert_topic'])
# kAdmin.list_consumer_groups(bootstrap_servers=servers)
kAdmin.list_consumer_group_offsets(bootstrap_servers=servers, group_ids=["SiemFlink_flink_rizhiyi"])

# kAdmin.describe_configs(bootstrap_servers=servers)
