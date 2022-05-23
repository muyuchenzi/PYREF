import psycopg2
from sqlalchemy import create_engine

cnn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='muyuchenzi',
                       user='chenzi', password="090359")

curs = cnn.cursor()
engin = create_engine("postgresql://postgre@127.0.0.1:5432/muyuchenzi")
