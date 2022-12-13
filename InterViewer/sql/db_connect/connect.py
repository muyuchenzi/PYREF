import pandas as pd
import psycopg2
import sqlalchemy


def con(sql_line):
    host = "localhost"
    port = 5432
    dbname = "test"
    user = "chenzi"
    password = "lizhenxiang"
    cnn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    cursor = cnn.cursor()
    cursor.execute(sql_line)
    cnn.commit()
    data = cursor.fetchall()
    return data
