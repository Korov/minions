import random

import pymysql.cursors
from loguru import logger

logger.add('mysql.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - {name}:{function}:{line} {message}",
           level="INFO")

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             database='database',
                             cursorclass=pymysql.cursors.DictCursor)

ids = []
while len(ids) < 500:
    ids.append(str(random.randrange(0, 10000000)))

where_id = "(" + str.join(", ", ids) + ")"
logger.info(where_id)

results = []

i = 0
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT * FROM `siem_loophole_log_migration_bak` limit 3000000, 800"
        sql = f"SELECT * FROM `siem_loophole_log_migration_bak` where id in {where_id}"
        # sql = "SELECT * FROM `siem_loophole_log_migration_bak` where id in (40000, 40001, 40002, 40003, 40004, 40005, 40006, 40007, 40008, 40009, 40010, 40011, 40012, 40013, 40014, 40015, 40016, 40017, 40018, 40019, 40020, 40021, 40022, 40023, 40024, 40025, 40026, 40027, 40028, 40029, 40030, 40031, 40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041, 40042, 40043, 40044, 40045, 40046, 40047, 40048, 40049, 40050, 40051, 40052, 40053, 40054, 40055, 40056, 40057, 40058, 40059, 40060, 40061, 40062, 40063, 40064, 40065, 40066, 40067, 40068, 40069, 40070, 40071, 40072, 40073, 40074, 40075, 40076, 40077, 40078, 40079, 40080, 40081, 40082, 40083, 40084, 40085, 40086, 40087, 40088, 40089, 40090, 40091, 40092, 40093, 40094, 40095, 40096, 40097, 40098, 40099, 40100, 40101, 40102, 40103, 40104, 40105, 40106, 40107, 40108, 40109, 40110, 40111, 40112, 40113, 40114, 40115, 40116, 40117, 40118, 40119, 40120, 40121, 40122, 40123, 40124, 40125, 40126, 40127, 40128, 40129, 40130, 40131, 40132, 40133, 40134, 40135, 40136, 40137, 40138, 40139, 40140, 40141, 40142, 40143, 40144, 40145, 40146, 40147, 40148, 40149, 40150, 40151, 40152, 40153, 40154, 40155, 40156, 40157, 40158, 40159, 40160, 40161, 40162, 40163, 40164, 40165, 40166, 40167, 40168, 40169, 40170, 40171, 40172, 40173, 40174, 40175, 40176, 40177, 40178, 40179, 40180, 40181, 40182, 40183, 40184, 40185, 40186, 40187, 40188, 40189, 40190, 40191, 40192, 40193, 40194, 40195, 40196, 40197, 40198, 40199, 40200, 40201, 40202, 40203, 40204, 40205, 40206, 40207, 40208, 40209, 40210, 40211, 40212, 40213, 40214, 40215, 40216, 40217, 40218, 40219, 40220, 40221, 40222, 40223, 40224, 40225, 40226, 40227, 40228, 40229, 40230, 40231, 40232, 40233, 40234, 40235, 40236, 40237, 40238, 40239, 40240, 40241, 40242, 40243, 40244, 40245, 40246, 40247, 40248, 40249, 40250, 40251, 40252, 40253, 40254, 40255, 40256, 40257, 40258, 40259, 40260, 40261, 40262, 40263, 40264, 40265, 40266, 40267, 40268, 40269, 40270, 40271, 40272, 40273, 40274, 40275, 40276, 40277, 40278, 40279, 40280, 40281, 40282, 40283, 40284, 40285, 40286, 40287, 40288, 40289, 40290, 40291, 40292, 40293, 40294, 40295, 40296, 40297, 40298, 40299, 40300, 40301, 40302, 40303, 40304, 40305, 40306, 40307, 40308, 40309, 40310, 40311, 40312, 40313, 40314, 40315, 40316, 40317, 40318, 40319, 40320, 40321, 40322, 40323, 40324, 40325, 40326, 40327, 40328, 40329, 40330, 40331, 40332, 40333, 40334, 40335, 40336, 40337, 40338, 40339, 40340, 40341, 40342, 40343, 40344, 40345, 40346, 40347, 40348, 40349, 40350, 40351, 40352, 40353, 40354, 40355, 40356, 40357, 40358, 40359, 40360, 40361, 40362, 40363, 40364, 40365, 40366, 40367, 40368, 40369, 40370, 40371, 40372, 40373, 40374, 40375, 40376, 40377, 40378, 40379, 40380, 40381, 40382, 40383, 40384, 40385, 40386, 40387, 40388, 40389, 40390, 40391, 40392, 40393, 40394, 40395, 40396, 40397, 40398, 40399, 40400, 40401, 40402, 40403, 40404, 40405, 40406, 40407, 40408, 40409, 40410, 40411, 40412, 40413, 40414, 40415, 40416, 40417, 40418, 40419, 40420, 40421, 40422, 40423, 40424, 40425, 40426, 40427, 40428, 40429, 40430, 40431, 40432, 40433, 40434, 40435, 40436, 40437, 40438, 40439, 40440, 40441, 40442, 40443, 40444, 40445, 40446, 40447, 40448, 40449, 40450, 40451, 40452, 40453, 40454, 40455, 40456, 40457, 40458, 40459, 40460, 40461, 40462, 40463, 40464, 40465, 40466, 40467, 40468, 40469, 40470, 40471, 40472, 40473, 40474, 40475, 40476, 40477, 40478, 40479, 40480, 40481, 40482, 40483, 40484, 40485, 40486, 40487, 40488, 40489, 40490, 40491, 40492, 40493, 40494, 40495, 40496, 40497, 40498, 40499)"
        cursor.execute(sql)
        old_result = cursor.fetchall()

        query_sql_list = []
        query_or_sql_list = []

        domain_name_set = set()
        name_set = set()
        source_set = set()
        hex_host_set = set()
        port_set = set()
        for result in old_result:
            domain_name = result['domain_name']
            domain_name = domain_name.replace("'", "\\'")
            domain_name_set.add(domain_name)
            name = result['name']
            name = name.replace("'", "\\'")
            name_set.add(name)
            source = result['source']
            source = source.replace("'", "\\'")
            source_set.add(source)
            hex_host_set.add(result['hex_host'])
            port_set.add(str(result['port']))
            query_sql = f"select * from siem_loophole_log_migration where(`hex_host`='{result['hex_host']}' and `port`={result['port']} and `domain_name`='{domain_name}' and `name`='{name}' and `source`='{source}')"
            query_sql_list.append(query_sql)
            query_or_sql = f"(`hex_host`='{result['hex_host']}' and `port`={result['port']} and `domain_name`='{domain_name}' and `name`='{name}' and `source`='{source}')"
            query_or_sql_list.append(query_or_sql)

        query_sql = str.join(" union \n", query_sql_list)
        logger.info(f"{query_sql};")

        query_or_sql = str.join(" or \n", query_or_sql_list)
        logger.info(f"select SQL_NO_CACHE * from siem_loophole_log_migration where {query_or_sql};")


        hex_host_set_sql = str.join("','", hex_host_set)
        hex_host_set_sql = f"`hex_host` in ('{hex_host_set_sql}')"
        port_set_sql = str.join(",", port_set)
        port_set_sql = f"`port` in ({port_set_sql})"
        domain_name_set_sql = str.join("','", domain_name_set)
        domain_name_set_sql = f"`domain_name` in ('{domain_name_set_sql}')"
        name_set_sql = str.join("','", name_set)
        name_set_sql = f"`name` in ('{name_set_sql}')"
        source_set_sql = str.join("','", source_set)
        source_set_sql = f"`source` in ('{source_set_sql}')"
        logger.info(f"select SQL_NO_CACHE * from siem_loophole_log_migration where {hex_host_set_sql} and \n{port_set_sql} and \n{domain_name_set_sql} and \n{name_set_sql} and \n{source_set_sql};")
