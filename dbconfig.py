import MySQLdb

conn = MySQLdb.connect(user="root", passwd="root", host="localhost", port=3306, db="crawling", charset='utf8')


def insert_sql(data_list):
    try:
        with conn.cursor() as curs:
            print("db 연결")
            # create_nm = "현대1"
            # carmd_nm = "아반떼1"
            # sql = 'insert into dbtest(create_nm, carmd_nm) values(%s, %s)'  # db 컬럼명을 생략하려면 values 에 컬럼만큼 값을 설정해 줘야되고 아니라면 명시를 해줘야함.
            # curs.execute(sql, [create_nm, carmd_nm])
            sql = 'insert into crawling_data1 values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
                  '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            curs.execute(sql, data_list)
            conn.commit()
    except:
        print("db 에러")
        print(curs.execute(sql))

    finally:
        conn.close()
