import psycopg2
import pandas as pd


# from operators.insert_score import insert_data


def db_connect():
    host = "localhost"
    port = 5432
    db_name = "test"
    user = "chenzi"
    password = "lizhenxiang"
    cnn = psycopg2.connect(host=host, port=port, dbname=db_name,
                           user=user, password=password)
    cusor = cnn.cursor()
    sql_line = read_sql_file()
    cusor.execute(sql_line)
    cnn.commit()
    data_get = cusor.fetchall()
    df = pd.DataFrame(data_get)
    return df


def read_sql_file():
    with open(r'E:\李震祥\PYGIT\PYref\module\SQL\PostgreSQL\50QA\temp.sql', mode="r", encoding='utf-8') as f:
        sql_lines = f.read()
    return sql_lines


if __name__ == '__main__':
    result = db_connect()
