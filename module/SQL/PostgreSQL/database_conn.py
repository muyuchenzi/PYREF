import psycopg2
import pandas as pd


def db_connect():
    """
    postgreSQL数据库的链接函数
    我的测试数据库为muyuchenzi
    账号:chenzi
    密码:lizhenxiang

    :return: 返回一个dataFrame
    """
    host = "localhost"
    port = 5432
    dbname = "muyuchenzi"
    user = "chenzi"
    password = "lizhenxiang"

    conn = psycopg2.connect(host=host, port=port, dbname=dbname,
                            user=user, password=password)

    curs = conn.cursor()
    select_sql = '''
                SELECT * FROM public.order_test
    '''
    curs.execute(select_sql)
    conn.commit()
    data = curs.fetchall()
    result = pd.DataFrame(data)
    return result
