import psycopg2
import pandas as pd
from operators.insert_score import insert_data


def db_connect():
    host = "localhost"
    port = 5432
    db_name = "test"
    user = "chenzi"
    password = "lizhenxiang"
    cnn = psycopg2.connect(host=host, port=port, dbname=db_name,
                           user=user, password=password)
    cusor = cnn.cursor()
    sql_line = insert_data()
    # cusor.execute(sql_line)
    cnn.commit()
    # data_get = cusor.fetchall()
    # df = pd.DataFrame(data_get)
    # return df


if __name__ == '__main__':
    result = db_connect()
