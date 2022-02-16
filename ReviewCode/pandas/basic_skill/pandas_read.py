# todo 数据的读取

import pandas as pd


def dataframe_read(file_path):
    xlsx_df = pd.read_excel(r'E:\李震祥\temp\pandas\Data\各省市订单数据.xlsx')
    csv_df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv')[['name', '订单数']]
    return csv_df, xlsx_df


def dataframe_output(data_frame):
    pass


def pandas_basic_functions(xlsx_df):
    for i in range(xlsx_df.shape[0]):
        xlsx_df.loc[i, 'name'] = i


def series_basic_functions(csv_df):
    series_01 = csv_df['名称']
    my_series = pd.Series([1, '2', 'x', 'y'])
    my_series2 = pd.Series([1, 2, 2, 3], index=['a', 'c', 'c', 'd'])
    series_to_dict = dict(zip(list(my_series.index), list(my_series.values)))
    dict_to_series = pd.Series(series_to_dict)
    type(dict_to_series[[1, 2]])
    my_pd = pd.DataFrame(my_series, columns=['value'])


def entrance_func():
    csv_df, xlsx_df = dataframe_read(r'E:\李震祥\temp\pandas\Data')
    # csv_df.rename(columns={'name': "名称", "订单数": "number"}, inplace=True)
    # csv_series = csv_df['名称']
    # csv_series2=csv_df[1:30:2]["名称"]
    series_basic_functions(csv_df)


if __name__ == '__main__':
    px = pd.DataFrame(data={'x': [1, 2, 3], 'y': [5, 6, 7], 'z': [8, 9, 0]})
