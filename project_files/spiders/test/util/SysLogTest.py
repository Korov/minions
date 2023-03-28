import logging.handlers

logger = logging.getLogger()
fh = logging.handlers.SysLogHandler(('192.168.50.27', 514), logging.handlers.SysLogHandler.LOG_AUTH)
formatter = logging.Formatter('%(message)s')

fh.setFormatter(formatter)
logger.addHandler(fh)
logger.error("<46>Feb 14 16:42:18 CENTER head:<185>2023-02-14 16:42:18 HiSec Insight %%01NORTHINTERFACE/1/COMMONTHREAT(l):An intrusion threat was detected. ,content:EventID=cef2d60c-6191-4a73-96b5-fb664acd19ea,EventClass=1514030,EventName=Information Disclosure Attack,EventLevel=3,EventCategory=13,EventSrcCategory=HiSec Insight,EventSrcIP=10.1.0.10,EventSrcName=,EventSrcType=Flowprobe,OccurTime=1676364137,ReporterIP=,SrcIP=192.168.201.4,SrcPort=55899,DestPort=7001,DestIP=192.168.1.249,SrcMac=,DestMac=,Protocol=TCP,OnThreatIP=192.168.1.249,DomainName=,FileName=,FileType=,FileMD5=,SrcArea=,DestArea=,SrcIPUser=,DestIPUser=,ThreatEventStatus=1,TenantID=00000000-0000-0000-0000-000000000000,TenantName=系统租户,ReceiveTime=1676364138268,RecentTime=1676364137,ReporterID=,EventType=12000,EventDigest=,NatSrcIP=,NatSrcPort=,NatDestIP=,NatDestPort=,Duration=,UpBytes=,DownBytes=,AppProtocol=HTTP,UserName=,OperType=,OperResult=,ObjectName=HTTP background scanning behavior detected,Reponse=,MergeCount=1,ProgramName=,RequestContent=,Action=2,DestServiceName=,DestHostName=,DestUserPrivileges=,DestProcessName=,DestUserId=,DestUserAccount=,ExternalID=,FileCreateTime=,FileModifyTime=,FilePath=,FilePermission=,OldFileCreateTime=,OldFileMD5=,OldFileModifyTime=,OldFileName=,OldFilePath=,OldFilePermission=,OldFileType=,RequestMethod=,SrcHostName=,SrcServiceName=,SrcUserPrivileges=,SrcProcessName=,SrcUserId=,SrcUserAccount=,OriginalData=aHR0cF91cmk6L2NvbnNvbGUvbG9naW4vTG9naW5Gb3JtLmpzcDs=,ThreatLevel=,RuleID=3bad8953-a951-49c9-a40e-751026d1effe,OriEventID=4b1291ff-0a39-49f9-b565-0447b65b0270,OriMetaDataID=677763eb4967004101000000,ConfidenceLevel=80,ParentThreatExist=,AtkDirection=1,AggregationEventID=,DestPortRange=,DataOutSendType=,FileDownType=,Reputation=,URL=http://192.168.1.249:7001/console/login/LoginForm.jsp,HttpRefer=,HttpUserAgent=,URLCategory=,MailReceivers=,MailSender=,MailID=,SrcGeographyLocationCountryOrRegion=,SrcGeographyLocationCity=,SrcGeographyLocationLongitude=,SrcGeographyLocationLatitude=,DestGeographyLocationCountryOrRegion=,DestGeographyLocationCity=,DestGeographyLocationLongitude=,DestGeographyLocationLatitude=,ReceiveDate=2023-02-14T08:42:18.312,OriEventType=,MailSubject=,MailAbstract=,MailReader=,MailServerName=,MailServerIP=,FileSize=,FileDirection=,ConnectPeriod=,SignatureID=694520,DomainIP=,SrcHostUniqueID=192.168.201.4,DstHostUniqueID=192.168.1.249,OnThreatHost=192.168.1.249,SubmitTime=,SubmitIP=,ParentMd5=,IsUnited=,SubmitSource=,AppType=,PolicyName=,PolicyId=,SubAppType=,VFWName=,VirusFamily=,VirusPlatform=,VirusType=,VirusName=,ProfileName=,ResponseCode=,threatName=,btwType=,EventSubType=12004,SystemCommand=,SrcProcessID=,DestProcessID=,AccountName=,AccountGroupID=,AccountGroupName=,TransactionTag=,CurrentDir=,AuditKey=,HitCount=1,ProtectObject=,AttackStatus=2,DropPackets=,DropKbits=,DataType=6,DetectType=1,OS=any,CveID=,BotnetRole=,MailSendTime=,文件Sha1=,FileSha256=,UrlMD5=,FileSubType=,IsThreatDecision=1,AttackPhase=16,ESN=,ThreatScore=,ReportSHA256=,IsDnsServer=,LocalVulID=,VulID=,VulName=,VulScanTargets=,VulPort=,MessString=,VulType=,VulScanTaskID=,PluginID=,VulCategory=,RiskPoints=,VulDescription=,VulSolution=,ScanTaskStartTime=,ScanTaskEndTime=,ScanTaskType=,ProductName=,ProductVersion=,VulLibVersion=,Vendor=,OriVulScanEventID=,SourceType=,SourceID=,AlarmCategory=,OriginalEventSrcIP=,SrcHostType=,DestHostType=,PortsQtyInPortScan=,AbnTrfBaseline=,ForensicsData=R0VUIC9jb25zb2xlL2xvZ2luL0xvZ2luRm9ybS5qc3AgSFRUUC8xLjENCkhvc3Q6IDE5Mi4xNjguMS4yNDk6NzAwMQ0KQWNjZXB0OiB0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjgNClVwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHM6IDENCkNvb2tpZTogQURNSU5DT05TT0xFU0VTU0lPTj1qeGRnNldGbEUyc2F6X0lGLUk0UTZrb3Q5TjRuTFpSZlZKVGFOamgtRlZRbzhzaGVDejdUIS0yMDQ4NDQ2ODcxOyBDTlpaREFUQTEyNTY3OTMyOTA9NTU0NTQ5NjYxLTE2MjUxMTc4NTAtJTdDMTYyNTEyMzI1MDsgSlNFU1NJT05JRD1xVGRnejE4aTdSNDU0WG9Qc19IcHdjR2lWRGNEamo0YXRFcEs4T0xRMVE2LTdJdkU2MVM4IS0yMDQ4NDQ2ODcxOyBVTV9kaXN0aW5jdGlkPTE3YTYwYjdjMjQ5NC0wNGU1ZjFjMjU5NjNkZS00OTE5MzEwMS0xM2M2ODAtMTdhNjBiN2MyNGFlM2QNClVzZXItQWdlbnQ6IE1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNC4xLjEgU2FmYXJpLzYwNS4xLjE1DQpBY2NlcHQtTGFuZ3VhZ2U6IHpoLWNuDQpBY2NlcHQtRW5jb2Rpbmc6IGd6aXAsIGRlZmxhdGUNCkNvbm5lY3Rpb246IGNsb3NlDQoNCg,ParentID=,CommandParams=,ConnectStatus=,AttackEvidenceID=000002000000017f0000000063eb4968,NetTag=,VRF=,ScannedIPs=,AttackerProfile=,Weapon=,AttackChain=,OnThreatAreaID=,AttackerIP=192.168.201.4,AttackerHostUniqueID=192.168.201.4,AttackerAreaID=,AttackerGeographyLocationCountryOrRegion=,AttackerGeographyLocationCity=,OnThreatAssetTypeId=5,IsHotEvent=,AssetType=,AssetStatus=,FirstAccess=,DeviceState=,ReportTime=,StartTime=,WiFiName=,WiFiIP=,WiFiMAC=,PatchID=,PatchName=,PatchPublishTime=,PatchLevel=,PatchCode=,PatchTime=,PatchState=,IsVM=,IsFeedBack=,EventDetailSrc=Correlation Analysis,XFF=,OnThreatRegionPath=-1,AttackerRegionPath=-1")