import os
import pandas as pd
import re
import numpy


def file_read(data_path):
    # NOTE 数据读取
    #  filepath or buffer(剪贴板)
    #  sep 分隔符，一般csv的分隔符为逗号，可能出现别人数据交换中异常情况。
    #  header 指定某一行作为列名，用于处理列名空缺
    #  name 用在读取dataFrame后表的列名显示，切记一定要与DataFrame的列名数量一直，否则容易出现问题。
    #  index_col 用于读取 设定选定某一列作为index
    #  skip_columns
    df = pd.read_csv(data_path)
    # NOTE dataFrame first five lines
    # print(df.head())
    # print(df.shape)
    return df


def files_in_path(path):
    '''
    NOTE 文件夹路径下的文件
    '''
    for dir_path, _, file_names in os.walk(path):
        print(file_names)
        print(dir_path)
        # print(sub_dir)  # 子文件夹


def file_out_path(path):
    # NOTE 输出文件夹，如果没有，则创建一个
    if not os.path.exists(path):
        os.mkdir(path)
        print("make result dir")
    else:
        print('dir has exists')


def df_merge(df1, df2):
    # NOTE 两个dataFrame进行根据字段拼接
    res_df = pd.merge(df1, df2, left_on='name', right_on='name',
                      how='inner', suffixes=("_df1", "_df2"), sort=True)
    # print(res_df.head())
    # print(res_df.shape)


def file_search(df):
    # NOTE
    # 取列数据  --注意查看结果是Series 还是DataFrame
    # 两种办法。
    series_column_alpha = df['name']
    series_column_beta = df.loc[:, "name"]
    dataframe_column_alpha = df[['name']]
    # 去行数据
    # 两种筛选方法。
    df_yunnan_alpha = df[df.loc[:, "省"] == "云南省", :]
    df_yunnan_beta = df[df['省'] == "云南省", :]
    df_yungui_alpha = df[(df.loc[:, "省"] == "云南省") | (
            df.loc[:, "省"] == "贵州省")][['name', "省"]]
    df_yungui_beta = df[(df['省'] == "云南省") | (df['省'] == '贵州省')][:]


def df_apply(df):
    '''
    #NOTE 一些简单 apply map 函数。
    '''
    df['省'] = df.apply(lambda x: x['省'].replace("省", ""), axis=1)
    print(df.head(10))
    df['市'] = df['城市简称'].map(lambda x: x.replace("市", ""))
    df['市_'] = df["城市简称"].str.replace("市", "")


def pre_process():
    '''
    #NOTE一些简单的对于na数据的处理
    '''
    df = pd.read_excel("E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\contain_na_data.xlsx", skiprows=3)
    df.dropna(how='all', axis=1, inplace=True)
    df.fillna(method='ffill', axis=0, inplace=True)


def group_by_func():
    '''
    #NOTE 针对某一列或者几列进行统计，agg为采用统计方法，
    '''
    df = pd.read_csv('E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv', encoding='utf-8')
    df_groupby = df.groupby(by=['省']).agg(({'订单数': 'mean', '包邮率': "min"})).reset_index(drop=False)
    df_groupby2 = df.groupby(by=['省', '城市等级']).agg({'订单数': 'mean', '包邮率': "min"}).reset_index(drop=False)
    df_pivot = df.pivot(index='省', columns='城市等级', values='订单数')


def pivot_table():
    '''#REVIEW
    数据透视表就是以某一列为index，另一列或者几列为columns，进行数据统计。
    '''
    df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                               'two'],
                       'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'baz': [1, 2, 3, 4, 5, 6],
                       'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

    df_pivot = df.pivot(index='foo', columns='bar', values='baz')


if __name__ == "__main__":
    order_data_path = 'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'
    data_path = 'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data'
    result_path = 'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Result'

    file_df = file_read(order_data_path)
    files_in_path(path=data_path)
    file_out_path(path=result_path)
    df_merge(file_df, file_df)

    # NOTE dataFrame的查询
    file_search(df=file_df)
    df_apply(file_df)
