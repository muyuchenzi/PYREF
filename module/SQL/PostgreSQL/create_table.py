# SQL 创建表格
# create table table_name(
#   字段1 数据格式,
#   字段2 数据格式
# )

create_table = """
create table public.teacher
(
    "教师号"  varchar,
    "教师名称" varchar
)
"""

# 数据的插入
insert_data = '''
insert into student("学号", "姓名", "出生日期", "性别") 
values ("001","猴子","1990-01-01","男");
'''
