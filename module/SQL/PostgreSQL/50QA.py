import pandas as pd
from sqlalchemy import create_engine
import psycopg2


def temp():
    engine = create_engine('postgresql+psycopg2://chenzi:lizhenxiang@localhost/test')
    df = pd.read_csv(r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv')
    df.to_sql("deletable", engine)


def cnn():
    host = "localhost"
    port = 5432
    dbname = "test"
    user = 'chenzi'
    password = "lizhenxiang"
    con = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname)
    cursor = con.cursor()
    sql_line = search_data()
    cursor.execute(sql_line)
    con.commit()
    data = cursor.fetchall()

    df = pd.DataFrame(data=data)


def search_data():
    sql_line = '''
    select * 
    from test.public.deletable
    '''
    return sql_line
