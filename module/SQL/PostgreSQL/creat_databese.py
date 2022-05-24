import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from database_conn import db_connect

conn = psycopg2.connect(host='localhost', port=5432, dbname='muyuchenzi',
                        user='chenzi', password="lizhenxiang")

curs = conn.cursor()

curs.execute(
    '''
    SELECT * FROM public.order_test
    '''
)
conn.commit()

rows = curs.fetchall()
res = pd.DataFrame(rows)
print(rows)


def main_in():
    result = db_connect()
    print(result)


if __name__ == '__main__':
    main_in()
