def sql_reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sql_lines = f.read()
    return sql_lines
