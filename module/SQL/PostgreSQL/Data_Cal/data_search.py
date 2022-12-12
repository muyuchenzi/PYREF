import psycopg2
import pandas as pd


def db_connect():
    """
    postgreSQL数据库的链接函数
    我的测试数据库为muyuchenzi
    账号:chenzi
    密码:lizhenxiang

    :return: 返回一个dataFrame
    """
    host = "localhost"
    port = 5432
    dbname = "muyuchenzi"
    user = "chenzi"
    password = "lizhenxiang"

    conn = psycopg2.connect(host=host, port=port, dbname=dbname,
                            user=user, password=password)

    curs = conn.cursor()
    # 001
    select_sql = db_search()
    # select_sql = sumary()

    curs.execute(select_sql)
    conn.commit()
    data = curs.fetchall()
    result = pd.DataFrame(data)
    print(result)


def db_search():
    '''
    简单查询
    :return:
    '''
    sql_alpha = '''select * from public.student where 姓名 like '猴%' '''
    sql_beta = '''select * from public.teacher where 教师姓名 like '孟%' '''
    return sql_alpha


def sumary():
    '''
    查询课程编号为“0002”的总成绩
    '''
    sql_alpha = '''
    select sum(成绩) from public.score  where 课程号='0002' 
    '''
    sql_beta = '''
    select count(distinct '学号') as 学生人数 from public.course
    '''
    return sql_beta


if __name__ == '__main__':
    db_connect()
