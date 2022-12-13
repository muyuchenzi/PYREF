import pandas as pd
from db_connect.connect import con
from db_connect.data_to_db import put_data
from db_connect.sql_reader import sql_reader


def sql_select():
    sql_file_path = r'E:\李震祥\PYGIT\PYref\InterViewer\sql\sql_files\search_temp.sql'
    sql_lines = sql_reader(file_path=sql_file_path)
    data = con(sql_line=sql_lines)
    result = pd.DataFrame(data=data)
    return result


def data_operators(df):
    df["add_columns"] = "xyz"
    return df


if __name__ == '__main__':
    res = sql_select()
    result_final = data_operators(res)
    put_data(result_final, table_name="temp")
