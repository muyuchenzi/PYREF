import pandas as pd


def csv_file_read():
    pass
    # todo pandas read_csv or read_excel 常用参数
    #  filepath or buffer(剪贴板)
    #  sep 分隔符，一般csv的分隔符为逗号，可能出现别人数据交换中异常情况。
    #  header 指定某一行作为列名，用于处理列名空缺
    #  name 用在读取dataFrame后表的列名显示，切记一定要与DataFrame的列名数量一直，否则容易出现问题。
    #  index_col 用于读取 设定选定某一列作为index
    #  skip_columns

    # csv_alpha = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv')
    # csv_alpha = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv', header=[1, 2])
    # csv_alpha = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv', names=['省', '订单数'])
    # csv_alpha = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.xlsx', index_col=['name'])
    csv_alpha = pd.read_excel(r'E:\李震祥\temp\pandas\Data\各省市订单数据.xlsx')

    # csv_alpha.to_excel(r'E:\李震祥\temp\pandas\Data\temp.xlsx', index=False, encoding='utf-9')
