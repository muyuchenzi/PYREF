from sqlalchemy import create_engine


# import psycopg2


def put_data(df, table_name):
    engine = create_engine("postgresql+psycopg2://chenzi:lizhenxiang@localhost/test")
    # engine = create_engine('postgresql+psycopg2://chenzi:lizhenxiang@localhost/test')
    df.to_sql(table_name, engine)
