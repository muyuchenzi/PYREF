import pandas as pd
from sqlalchemy import create_engine
import psycopg2


def cnn():
    '''
    :return:
    '''
    host = "localhost"
    port = 5432
    db_name = "test"
    user = "chenzi"
    password = "lizhenxiang"
    cnn = psycopg2.connect(host=host, port=port, dbname=db_name,
                           user=user, password=password)
    return cnn
