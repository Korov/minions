import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='user',
                             database='pwssword',
                             user='user',
                             password='paswsword',
                             database='database',
                             cursorclass=pymysql.cursors.DictCursor)

results = []

i = 0
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `siem_loophole_log`"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
        old_result = cursor.fetchall()

        for result in old_result:
            results.append(result)

    with connection.cursor() as cursor:
        for index in range(0, 200):
            values = []
            for result in results:
                i = i + 1
                tup = (result['host'], result['hex_host'], result['domain_name'] + str(i),
                       -1 if (result['port'] is None) else result['port'], result['asset_name'],
                       result['owner_name'], result['name'], result['risk_level'],
                       result['siem_risk_level'], result['loophole_id'],
                       result['source'], result['source_id'],
                       result['status'], result['scan_id'], result['scan_host'],
                       result['scanner_start_time'], result['scanner_end_time'],
                       result['last_scan_time'], result['create_time'], result['update_time'])  # 构造元组

                # values.append(f"""('{result['host']}', '{result['hex_host']}', '{result['domain_name'] + str(i)}',
                #             {-1 if (result['port'] is None) else result['port']}, '{result['asset_name']}',
                #         '{result['owner_name']}', '{result['name']}', {result['risk_level']},
                #                           {result['siem_risk_level']}, '{result['loophole_id']}',
                #                           '{result['source']}', '{result['source_id']}',
                #                           {result['status']}, '{result['scan_id']}', '{result['scan_host']}',
                #                            '{result['scanner_start_time']}', '{result['scanner_end_time']}',
                #                            '{result['last_scan_time']}', '{result['create_time']}',
                #                           '{result['update_time']}')""")
                values.append(tup)

            # insert_value = ",".join(values)
            insert_sql = """insert into siem_loophole_log(host, hex_host, domain_name, port, asset_name, owner_name, name, risk_level,
                                                                          siem_risk_level, loophole_id, source, source_id, status, scan_id, scan_host,
                                                                          scanner_start_time, scanner_end_time, last_scan_time, create_time, update_time)
                                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            # print(insert_sql)
            print(f"index:{index}, size:{len(values)}")
            cursor.executemany(insert_sql, values)
            connection.commit()

            # print(f"""host:{result['host']}, hex_host:{result['hex_host']}, domain_name:{result['domain_name']},
            #     port:{result['port']}, asset_name:{result['asset_name']},
            # owner_name:{result['owner_name']}, name:{result['name']}, risk_level:{result['risk_level']},
            #                   siem_risk_level:{result['siem_risk_level']}, loophole_id:{result['loophole_id']},
            #                   source:{result['source']}, source_id:{result['source_id']},
            #                   status:{result['status']}, scan_id:{result['scan_id']}, scan_host:{result['scan_host']},
            #                    scanner_start_time:{result['scanner_start_time']}, scanner_end_time:{result['scanner_end_time']},
            #                    last_scan_time:{result['last_scan_time']}, create_time:{result['create_time']},
            #                   update_time:{result['update_time']}""")

