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


def insert_datas():
    datas = [["0005", "muyu", "1999-9-9", "男"], ["0006", "chenzi", "1999-9-22", "女"]]
    for data in datas:
        insert_vals = '''
        insert into test.public.student("学号", "姓名", "出生日期", "性别")
        values (data[0],data[1],data[2],data[3])'''


if __name__ == '__main__':
    insert_datas()
