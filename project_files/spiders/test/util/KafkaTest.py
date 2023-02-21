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
kProducer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="flink_alert", msg='{"agent_send_timestamp":1676541714878,"collector_recv_timestamp":1676541714878,"raw_message":"<46>Feb 14 17:53:59 CENTER head:<185>2023-02-14 17:53:59 HiSec Insight %%01NORTHINTERFACE/1/COMMONTHREAT(l):An intrusion threat was detected. ,content:EventID=11d312af-fa8a-48fb-abef-454c85599052,EventClass=1514057,EventName=Command Execution Attack,EventLevel=4,EventCategory=13,EventSrcCategory=HiSec Insight,EventSrcIP=10.1.0.10,EventSrcName=,EventSrcType=Flowprobe,OccurTime=1676368438,ReporterIP=,SrcIP=188.158.116.177,SrcPort=56212,DestPort=7001,DestIP=192.168.183.224,SrcMac=,DestMac=,Protocol=TCP,OnThreatIP=192.168.183.224,DomainName=,FileName=,FileType=,FileMD5=,SrcArea=,DestArea=,SrcIPUser=,DestIPUser=,ThreatEventStatus=1,TenantID=00000000-0000-0000-0000-000000000000,TenantName=系统租户,ReceiveTime=1676368439333,RecentTime=1676368438,ReporterID=,EventType=2000,EventDigest=,NatSrcIP=,NatSrcPort=,NatDestIP=,NatDestPort=,Duration=,UpBytes=,DownBytes=,AppProtocol=HTTP,UserName=,OperType=,OperResult=,ObjectName=Oracle WebLogic Server Unauthenticated Command Execution,Reponse=,MergeCount=1,ProgramName=,RequestContent=,Action=2,DestServiceName=,DestHostName=,DestUserPrivileges=,DestProcessName=,DestUserId=,DestUserAccount=,ExternalID=,FileCreateTime=,FileModifyTime=,FilePath=,FilePermission=,OldFileCreateTime=,OldFileMD5=,OldFileModifyTime=,OldFileName=,OldFilePath=,OldFilePermission=,OldFileType=,RequestMethod=,SrcHostName=,SrcServiceName=,SrcUserPrivileges=,SrcProcessName=,SrcUserId=,SrcUserAccount=,OriginalData=aHR0cF9yYXdfdXJpOi9jb25zb2xlL2Nzcy8lMjUyZSUyNTJlJTI1MmZjb25zb2xlLnBvcnRhbD9fbmZwYj10cnVlJl9wYWdlTGFiZWw9JmhhbmRsZT1jb20uYmVhLmNvcmUucmVwYWNrYWdlZC5zcHJpbmdmcmFtZXdvcmsuY29udGV4dC5zdXBwb3J0LkZpbGVTeXN0ZW1YbWxBcHBsaWNhdGlvbkNvbnRleHQoJTIyaHR0cDovLzE5NC4=,ThreatLevel=,RuleID=79bc6db6-804a-40ed-879d-00a94c8705d7,OriEventID=0c66c6ee-879e-4cb5-9185-ab3ca9c53af8,OriMetaDataID=becb63eb5a36004201000000,ConfidenceLevel=80,ParentThreatExist=,AtkDirection=1,AggregationEventID=,DestPortRange=,DataOutSendType=,FileDownType=,Reputation=,URL=http://192.168.183.224/tags,HttpRefer=,HttpUserAgent=,URLCategory=,MailReceivers=,MailSender=,MailID=,SrcGeographyLocationCountryOrRegion=,SrcGeographyLocationCity=,SrcGeographyLocationLongitude=,SrcGeographyLocationLatitude=,DestGeographyLocationCountryOrRegion=,DestGeographyLocationCity=,DestGeographyLocationLongitude=,DestGeographyLocationLatitude=,ReceiveDate=2023-02-16 17:47:27,OriEventType=,MailSubject=,MailAbstract=,MailReader=,MailServerName=,MailServerIP=,FileSize=,FileDirection=,ConnectPeriod=,SignatureID=609710,DomainIP=,SrcHostUniqueID=188.158.116.177,DstHostUniqueID=192.168.183.224,OnThreatHost=192.168.183.224,SubmitTime=,SubmitIP=,ParentMd5=,IsUnited=,SubmitSource=,AppType=,PolicyName=,PolicyId=,SubAppType=,VFWName=,VirusFamily=,VirusPlatform=,VirusType=,VirusName=,ProfileName=,ResponseCode=,threatName=,btwType=,EventSubType=2027,SystemCommand=,SrcProcessID=,DestProcessID=,AccountName=,AccountGroupID=,AccountGroupName=,TransactionTag=,CurrentDir=,AuditKey=,HitCount=1,ProtectObject=,AttackStatus=2,DropPackets=,DropKbits=,DataType=6,DetectType=1,OS=any,CveID=CVE-2022-12021,BotnetRole=,MailSendTime=,文件Sha1=,FileSha256=,UrlMD5=,FileSubType=,IsThreatDecision=1,AttackPhase=16,ESN=,ThreatScore=,ReportSHA256=,IsDnsServer=,LocalVulID=,VulID=,VulName=,VulScanTargets=,VulPort=,MessString=,VulType=,VulScanTaskID=,PluginID=,VulCategory=,RiskPoints=,VulDescription=,VulSolution=,ScanTaskStartTime=,ScanTaskEndTime=,ScanTaskType=,ProductName=,ProductVersion=,VulLibVersion=,Vendor=,OriVulScanEventID=,SourceType=,SourceID=,AlarmCategory=,OriginalEventSrcIP=,SrcHostType=,DestHostType=,PortsQtyInPortScan=,AbnTrfBaseline=,ForensicsData,ParentID=,CommandParams=,ConnectStatus=,AttackEvidenceID=00000200000001910000000063eb5a36,NetTag=,VRF=,ScannedIPs=,AttackerProfile=,Weapon=,AttackChain=,OnThreatAreaID=,AttackerIP=188.158.116.177,AttackerHostUniqueID=188.158.116.177,AttackerAreaID=,AttackerGeographyLocationCountryOrRegion=,AttackerGeographyLocationCity=,OnThreatAssetTypeId=5,IsHotEvent=,AssetType=,AssetStatus=,FirstAccess=,DeviceState=,ReportTime=,StartTime=,WiFiName=,WiFiIP=,WiFiMAC=,PatchID=,PatchName=,PatchPublishTime=,PatchLevel=,PatchCode=,PatchTime=,PatchState=,IsVM=,IsFeedBack=,EventDetailSrc=Correlation Analysis,XFF=,OnThreatRegionPath=-1,AttackerRegionPath=-1","index":"ops-yotta-20230216","logical_index":"yotta","logtype":"hisec","hostname":"192.168.201.9","appname":"hisec","domain":"ops","context_id":1676541714878014889,"hisec":{"OriEventID__s__":"0c66c6ee-879e-4cb5-9185-ab3ca9c53af8","AttackPhase__s__":"16","ConfidenceLevel__s__":"80","OriMetaDataID__s__":"becb63eb5a36004201000000","AttackerIP":{"geo":{"longitude__d__":53.69291,"isp__s__":"Parvaresh Dadeha Co. Private Joint Stock","country__s__":"伊朗","ip__s__":"188.158.116.177","latitude__d__":32.42316,"province__s__":"*","city__s__":"*"}},"AbnTrfBaseline__s__":",ForensicsData","principleCn__s__":"扫描开放445文件共享端口的Windows机器，利用该漏洞传播恶意软件。","AtkDirection__s__":"1","handleSuggestCn__s__":"1、【遏制】：将受威胁主机进行隔离，断开网络连接，防止恶意行为进一步扩散。2、【溯源】：搜索受威胁主机的历史事件，查看是否包含web扫描事件，以确认事件的攻击来源。3、【清理】：根据操作系统类型，下载并安装对应的永恒之蓝补丁文件，完成后恢复该主机的网络连接。4、【预防】：（1）在系统中部署漏洞扫描产品，定期检查是否存在漏洞，对主机进行安全加固，及时更新补丁，防止攻击者利用漏洞进行攻击；在网络入口处配置防火墙等安全设备，减少恶意入侵的可能；（2）提高员工的安全意识，对来历不明的邮件中的附件、从网络下载后未经杀毒处理的软件慎重打开。","ReceiveTime__s__":"1676368439333","MergeCount__s__":"1","EventCategory__s__":"13","impactCn__s__":"永恒之蓝利用Windows系统的SMB漏洞可以获取系统最高权限。恶意代码会扫描开放445文件共享端口的Windows机器，无需用户任何操作，只要开机上网，不法分子就能在电脑和服务器中植入勒索软件、远程控制木马、虚拟货币挖矿机等恶意程序。    ","AttackStatus__s__":"2","OnThreatHost__s__":"192.168.183.224","EventSubType__s__":"2027","EventDetailSrc__s__":"Correlation Analysis","CveID__s__":"CVE-2022-12021","EventSrcType__s__":"Flowprobe","HitCount__s__":"1","OccurTime__s__":"1676368438","Protocol__s__":"TCP","TenantName__s__":"系统租户","RuleID__s__":"79bc6db6-804a-40ed-879d-00a94c8705d7","AttackEvidenceID__s__":"00000200000001910000000063eb5a36","SrcIP__s__":"188.158.116.177","SrcHostUniqueID__s__":"188.158.116.177","ObjectName__s__":"Oracle WebLogic Server Unauthenticated Command Execution","EventSrcCategory__s__":"HiSec Insight","threatNameCn__s__":"永恒之蓝","AppProtocol__s__":"HTTP","SrcPort__s__":"56212","threatDigestCn__s__":"攻击者（[AttackerIP]）利用永恒之蓝漏洞向受害者（[OnThreatIP]）发起了攻击，攻击事件名称（[ObjectName]），网络设备类型（[EventSrcType]），网络设备IP（[EventSrcIP]）。","EventClass__s__":"1514057","ReceiveDate__s__":"2023-02-16 17:47:27","OnThreatIP__s__":"192.168.183.224","EventSrcIP__s__":"10.1.0.10","OS__s__":"any","AttackerHostUniqueID__s__":"188.158.116.177","TenantID__s__":"00000000-0000-0000-0000-000000000000","Action__s__":"2","SignatureID__s__":"609710","URL__s__":"http://192.168.183.224/tags","DataType__s__":"6","DstHostUniqueID__s__":"192.168.183.224","AttackerRegionPath__s__":"-1","DetectType__s__":"1","RecentTime__s__":"1676368438","OnThreatAssetTypeId__s__":"5","EventName__s__":"Command Execution Attack","ThreatEventStatus__s__":"1","EventLevel__s__":"4","OnThreatRegionPath__s__":"-1","EventType__s__":"2000","EventID__s__":"11d312af-fa8a-48fb-abef-454c85599052","DestIP__s__":"192.168.183.224","DestPort__s__":"7001","IsThreatDecision__s__":"1"},"tag":["hisec"],"id":"AYZZrGG-wjsgtcpoyfWr","raw_message_length":4262,"timestamp":1676541714878}')
#
# kAdmin.list_topics(bootstrap_servers=servers)
# kAdmin.describe_topics(bootstrap_servers=servers, topics=['alert_topic'])
# kAdmin.list_consumer_groups(bootstrap_servers=servers)
# kAdmin.list_consumer_group_offsets(bootstrap_servers=servers, group_ids=["monitor"])

# kAdmin.describe_configs(bootstrap_servers=servers)
