import psycopg2
import pandas as pd


def search_datas():
    '''
    :return:查询语句
    '''
    # search_line = '''
    # select *
    # from muyuchenzi.public.student'''
    search_line_beta = '''
    select *
    from test.public.student'''
    return search_line_beta


def search_columns():
    line = '''
    select column_name
    from test.public.student'''
    return line


def db_connect():
    host = "localhost"
    port = "5432"
    db_name = "test"
    user = "chenzi"
    password = "lizhenxiang"

    cnn = psycopg2.connect(host=host, port=port, dbname=db_name,
                           user=user, password=password)
    cursor = cnn.cursor()

    sql_line = search_datas()
    sql_line = search_columns()
    cursor.execute(sql_line)
    cnn.commit()
    datas = cursor.fetchall()
    datas = pd.DataFrame(datas)
    return datas


if __name__ == '__main__':
    result = db_connect()
