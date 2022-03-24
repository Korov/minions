import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='user',
                             database='pwssword',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `siem_loophole_log`"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
