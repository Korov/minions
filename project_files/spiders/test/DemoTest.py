import random

from loguru import logger

#
# location = '/home/korov/Desktop/gitrepo/minions/project_files/spiders/fake_useragent.json'
# logger.info(location)
# ua = UserAgent(use_cache_server=False, verify_ssl=False)
#
# logger.info(ua.random)
# value = "aa'ff'afe"
# ids = set()
# while len(ids) < 500:
#     ids.add(str(random.randrange(0, 10000000)))
# logger.info("('" + str.join("', '", ids) + "')")

print(b'{\n "_alert_domain_id": 1,\n "_alert_domain_token": "79f56985674332a432b5e6e2b9d87b52",\n "_alert_history_id": "4634_1671176920945_0",\n "_alert_id": 4634,\n "_alert_owner_id": 1,\n "_alert_owner_name": "admin",\n "_alert_plugins": [],\n "check_interval": 60000,\n "description": "",\n "exec_time": 1671176921287.0,\n "extend_conf": {},\n "graph_enabled": false,\n "is_alert_recovery": false,\n "is_segmentation": false,\n "level": "mid",\n "name": "SNMP_\xe7\xbc\xba\xe7\x9c\x81\xe5\x8f\xa3\xe4\xbb\xa4",\n "plugin": [],\n "resource_groups": [],\n "result": {\n "columns": [\n {\n "name": "dst_ip",\n "groupby": true,\n "type": "UNKNOWN"\n },\n {\n "name": "src_ip",\n "groupby": true,\n "type": "UNKNOWN"\n },\n {\n "name": "cnt",\n "groupby": false,\n "type": "LONG"\n },\n {\n "name": "src_addr",\n "source": "EVAL",\n "type": "UNKNOWN"\n },\n {\n "name": "dst_addr",\n "source": "EVAL",\n "type": "UNKNOWN"\n },\n {\n "name": "inner_event",\n "source": "EVAL",\n "type": "INT"\n }\n ],\n "extend_hits": [],\n "extend_result": {},\n "extend_result_sheets_total": 0,\n "extend_result_total_hits": 0,\n "extend_total": 0,\n "hits": [\n {\n "src_ip": "192.168.1.130",\n "inner_event": 1,\n "dst_addr": "192.168.1.22",\n "cnt": 1,\n "src_addr": "192.168.1.130",\n "dst_ip": "192.168.1.22"\n },\n {\n "src_ip": "2409:8038:2000:2070:0:0:0:1",\n "inner_event": 1,\n "dst_addr": "2409:8038:2000:1103:0:0:0:1",\n "cnt": 1,\n "src_addr": "2409:8038:2000:2070:0:0:0:1",\n "dst_ip": "2409:8038:2000:1103:0:0:0:1"\n }\n ],\n "is_extend_query_timechart": false,\n "total": 2,\n "value": 1.0\n },\n "search": {\n "datasets": "[]",\n "extend_datasets": "[]",\n "query": "appname:ids AND event_name:SNMP_\xe7\xbc\xba\xe7\x9c\x81\xe5\x8f\xa3\xe4\xbb\xa4*|stats count() as cnt by dst_ip ,src_ip|mvcombine sep=\\";\\" src_ip\\n|eval src_addr=src_ip|eval dst_addr=dst_ip|eval inner_event=1"\n },\n "send_time": 1671176922418.0,\n "strategy": {\n "description": "SPL\xe5\x91\x8a\xe8\xad\xa6",\n "name": "spl_query",\n "trigger": {\n "alert_thresholds": "{\\"mid\\":[0.0]}",\n "category": 4,\n "compare": ">",\n "compare_style": "fixed",\n "compare_value": [\n 0.0\n ],\n "end_time": 1671176920945.0,\n "field": "cnt",\n "level": "mid",\n "start_time": 1671176860945.0,\n "time_range": "-1",\n "time_range_unit": "m"\n }\n },\n "traceid": "Alert_4634_1671176920945",\n "trigger_timestamp": 1671176920945\n}'.decode())


