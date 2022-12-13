import pandas as pd
import psycopg2
from sqlalchemy import create_engine


def cnn():
    host = "localhost"
    port = 5432
    db_name = "test"
    user = "chenzi"
    password = "lizhenxiang"
    cnn = psycopg2.connect(host=host, port=port, dbname=db_name,
                           user=user, password=password)
    return cnn


def engine_get():
    engine = create_engine('postgresql+psycopg2://chenzi:lizhenxiang@localhost/test')
    return engine


def insert_data():
    df = pd.read_csv(r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\data.csv', encoding='utf-8')
    engine = engine_get()
    df.to_sql("data_exercise", engine)


if __name__ == '__main__':
    insert_data()
