import random
import uuid

import pymysql.cursors
from loguru import logger

logger.add('mysql_insert.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rizhiyi&2014',
                             database='rizhiyi_system',
                             cursorclass=pymysql.cursors.DictCursor)


def insert_with_id():
    drop_table_sql = """drop table if exists siem_loophole_log_migration_insert_id;"""
    create_table_sql = """CREATE TABLE if not exists `siem_loophole_log_migration_insert_id` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `host` varchar(39) NOT NULL DEFAULT '' COMMENT '漏洞发现地址',
  `hex_host` char(32) NOT NULL DEFAULT '' COMMENT '漏洞发现地址对应十六进制',
  `domain_name` varchar(255) NOT NULL DEFAULT '' COMMENT '域名',
  `port` int NOT NULL DEFAULT '-1' COMMENT '端口',
  `asset_name` varchar(128) DEFAULT '' COMMENT '关联资产名称',
  `owner_name` varchar(128) DEFAULT '' COMMENT '关联资产负责人名称',
  `name` varchar(256) NOT NULL DEFAULT '' COMMENT '漏洞名',
  `risk_level` tinyint DEFAULT NULL COMMENT '漏洞原始等级',
  `siem_risk_level` tinyint DEFAULT NULL COMMENT '漏洞危险等级，低：0，中：1，高：2',
  `loophole_id` varchar(32) NOT NULL COMMENT '漏洞信息详细信息id',
  `source_type` tinyint NOT NULL DEFAULT '0' COMMENT '漏洞类型：0（扫描器），1（人工）',
  `source` varchar(32) NOT NULL DEFAULT '' COMMENT '漏洞数据来源',
  `source_id` varchar(128) NOT NULL DEFAULT '',
  `status` tinyint NOT NULL DEFAULT '0' COMMENT '漏洞处理情况，(未修复:0, 已修复:1, 忽略:2)',
  `scan_id` varchar(20) NOT NULL COMMENT '扫描id',
  `scan_host` char(20) NOT NULL DEFAULT '' COMMENT '漏洞发现地址',
  `description_id` bigint DEFAULT NULL COMMENT '漏洞描述对应siem_loophole_text_value表的id',
  `solution_id` bigint DEFAULT NULL COMMENT '解决方案对应siem_loophole_text_value表的id',
  `disposal_recommendations_id` bigint DEFAULT NULL COMMENT '处置建议对应siem_loophole_text_value表的id',
  `cve_time` datetime DEFAULT NULL COMMENT 'cve发布时间',
  `cve_id` varchar(256) NOT NULL DEFAULT '' COMMENT '全称Common Vulnerabilities & Exposures,公共漏洞和暴露的编号',
  `cnnvd_id` varchar(32) NOT NULL DEFAULT '' COMMENT '国家信息安全漏洞库编号id',
  `cncve_id` varchar(32) NOT NULL DEFAULT '' COMMENT '国家cve编号id',
  `cnvd_id` varchar(32) NOT NULL DEFAULT '' COMMENT '国家信息安全漏洞共享平台编号id',
  `bugtraq` varchar(32) NOT NULL DEFAULT '' COMMENT '计算机安全漏洞邮件编号',
  `cvss` decimal(13,4) DEFAULT NULL COMMENT '漏洞评分',
  `discovery_time` datetime NOT NULL COMMENT '发现时间',
  `last_scan_time` datetime NOT NULL COMMENT '最后扫描时间',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_host_port_domain_name_loophole_name_source` (`hex_host`,`port`,`domain_name`,`name`,`source`),
  KEY `idx_loophole_name` (`name`(255)),
  KEY `idx_loophole_id` (`loophole_id`),
  KEY `idx_scan_id` (`scan_id`),
  KEY `idx_last_scan_time` (`last_scan_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='漏洞扫描信息表';"""
    with connection.cursor() as cursor:
        cursor.execute(drop_table_sql)
        cursor.execute(create_table_sql)

        for index in range(1, 100000):
            domain_name = str(random.randrange(1, 500000))
            name = "openssl \"ssl-death-alert\" 拒绝服务漏洞(cve-2016-8610)【原理扫描】" + str(index)
            insert_with_id_sql = f"""INSERT INTO siem_loophole_log_migration_insert_id (host, hex_host, domain_name, port, asset_name, owner_name, name,
                                         risk_level, siem_risk_level, loophole_id, source_type, source, source_id,
                                         status, scan_id, scan_host, description_id, solution_id,
                                         disposal_recommendations_id, cve_time, cve_id, cnnvd_id, cncve_id, cnvd_id,
                                         bugtraq, cvss, discovery_time, last_scan_time, create_time, update_time)
VALUES ('112.17.34.91', '0000000000000000000000007011225B', '{domain_name}', -1, null, null,
        '{name}', 2, 2, 'RSAS777_76960_112.17.34.91', 0, 'rsas', '', 0,
        'RSAS777_76960_112.17', '', 1223, 580, null, '2022-03-25 11:41:21', 'CVE-2016-8610', '', '', '', '', null,
        '2021-04-24 08:47:38', '2021-04-24 08:47:38', '2022-03-09 16:21:34', '2022-03-09 16:21:34');"""
            cursor.execute(insert_with_id_sql)
            connection.commit()
            logger.info(f"insert with index:{index}")


def insert_with_uui():
    drop_table_sql = """drop table if exists siem_loophole_log_migration_insert_uuid;"""
    create_table_sql = """CREATE TABLE if not exists `siem_loophole_log_migration_insert_uuid` (
      `id`                          char(36)     NOT NULL COMMENT '自增id',
      `host` varchar(39) NOT NULL DEFAULT '' COMMENT '漏洞发现地址',
      `hex_host` char(32) NOT NULL DEFAULT '' COMMENT '漏洞发现地址对应十六进制',
      `domain_name` varchar(255) NOT NULL DEFAULT '' COMMENT '域名',
      `port` int NOT NULL DEFAULT '-1' COMMENT '端口',
      `asset_name` varchar(128) DEFAULT '' COMMENT '关联资产名称',
      `owner_name` varchar(128) DEFAULT '' COMMENT '关联资产负责人名称',
      `name` varchar(256) NOT NULL DEFAULT '' COMMENT '漏洞名',
      `risk_level` tinyint DEFAULT NULL COMMENT '漏洞原始等级',
      `siem_risk_level` tinyint DEFAULT NULL COMMENT '漏洞危险等级，低：0，中：1，高：2',
      `loophole_id` varchar(32) NOT NULL COMMENT '漏洞信息详细信息id',
      `source_type` tinyint NOT NULL DEFAULT '0' COMMENT '漏洞类型：0（扫描器），1（人工）',
      `source` varchar(32) NOT NULL DEFAULT '' COMMENT '漏洞数据来源',
      `source_id` varchar(128) NOT NULL DEFAULT '',
      `status` tinyint NOT NULL DEFAULT '0' COMMENT '漏洞处理情况，(未修复:0, 已修复:1, 忽略:2)',
      `scan_id` varchar(20) NOT NULL COMMENT '扫描id',
      `scan_host` char(20) NOT NULL DEFAULT '' COMMENT '漏洞发现地址',
      `description_id` bigint DEFAULT NULL COMMENT '漏洞描述对应siem_loophole_text_value表的id',
      `solution_id` bigint DEFAULT NULL COMMENT '解决方案对应siem_loophole_text_value表的id',
      `disposal_recommendations_id` bigint DEFAULT NULL COMMENT '处置建议对应siem_loophole_text_value表的id',
      `cve_time` datetime DEFAULT NULL COMMENT 'cve发布时间',
      `cve_id` varchar(256) NOT NULL DEFAULT '' COMMENT '全称Common Vulnerabilities & Exposures,公共漏洞和暴露的编号',
      `cnnvd_id` varchar(32) NOT NULL DEFAULT '' COMMENT '国家信息安全漏洞库编号id',
      `cncve_id` varchar(32) NOT NULL DEFAULT '' COMMENT '国家cve编号id',
      `cnvd_id` varchar(32) NOT NULL DEFAULT '' COMMENT '国家信息安全漏洞共享平台编号id',
      `bugtraq` varchar(32) NOT NULL DEFAULT '' COMMENT '计算机安全漏洞邮件编号',
      `cvss` decimal(13,4) DEFAULT NULL COMMENT '漏洞评分',
      `discovery_time` datetime NOT NULL COMMENT '发现时间',
      `last_scan_time` datetime NOT NULL COMMENT '最后扫描时间',
      `create_time` datetime NOT NULL COMMENT '创建时间',
      `update_time` datetime DEFAULT NULL COMMENT '更新时间',
      PRIMARY KEY (`id`),
      UNIQUE KEY `uk_host_port_domain_name_loophole_name_source` (`hex_host`,`port`,`domain_name`,`name`,`source`),
      KEY `idx_loophole_name` (`name`(255)),
      KEY `idx_loophole_id` (`loophole_id`),
      KEY `idx_scan_id` (`scan_id`),
      KEY `idx_last_scan_time` (`last_scan_time`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='漏洞扫描信息表';"""
    with connection.cursor() as cursor:
        cursor.execute(drop_table_sql)
        cursor.execute(create_table_sql)

        for index in range(1, 100000):
            id = uuid.uuid4().__str__()
            domain_name = str(random.randrange(1, 500000))
            name = "openssl \"ssl-death-alert\" 拒绝服务漏洞(cve-2016-8610)【原理扫描】" + str(index)
            insert_with_id_sql = f"""INSERT INTO siem_loophole_log_migration_insert_uuid (id, host, hex_host, domain_name, port, asset_name, owner_name, name,
                                             risk_level, siem_risk_level, loophole_id, source_type, source, source_id,
                                             status, scan_id, scan_host, description_id, solution_id,
                                             disposal_recommendations_id, cve_time, cve_id, cnnvd_id, cncve_id, cnvd_id,
                                             bugtraq, cvss, discovery_time, last_scan_time, create_time, update_time)
    VALUES ('{id}', '112.17.34.91', '0000000000000000000000007011225B', '{domain_name}', -1, null, null,
            '{name}', 2, 2, 'RSAS777_76960_112.17.34.91', 0, 'rsas', '', 0,
            'RSAS777_76960_112.17', '', 1223, 580, null, '2022-03-25 11:41:21', 'CVE-2016-8610', '', '', '', '', null,
            '2021-04-24 08:47:38', '2021-04-24 08:47:38', '2022-03-09 16:21:34', '2022-03-09 16:21:34');"""
            cursor.execute(insert_with_id_sql)
            connection.commit()
            logger.info(f"insert with index:{index}")


if __name__ == "__main__":
    insert_with_uui()
