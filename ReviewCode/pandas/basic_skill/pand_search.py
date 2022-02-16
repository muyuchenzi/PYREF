import pandas as pd

csv_pd = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv', encoding='utf-8')

xx = csv_pd.loc[:, "name"]
result = pd.DataFrame(columns=['name'])
result['name'] = csv_pd.apply(lambda x: x["name"] + "res", axis=1)

# 1、查询列 范围Series
df_colu_alpha = csv_pd.loc[:, "name"]  # 返回一个Series
df_colu_beta = csv_pd['name']

# 2、拿到 DataFrame
xx=csv_pd['省'] == '云南省'
df_yun = csv_pd[csv_pd['省'] == '云南省']
df_yun_2 = csv_pd.loc[csv_pd['省'] == '云南省', :]
df_yungui = csv_pd.loc[(csv_pd['省'] == '云南省') | (csv_pd['省'] == '贵州省'), :]
df_yungui_2 = csv_pd.loc[lambda x: (x['省'] == '云南省') | (x['省'] == '贵州省'), :]
# df_result=csv_pd.loc[function(df),:] function 返回 T

assert df_colu_beta == df_colu_alpha
# def common_funcition(csv_pd):
#     '''
#     常用方法
#     '''
#     # csv_slice = csv_pd[['name']]
#     # csv_series = csv_pd['name']
#
#     # csv_slice.loc[:, '名称'] = csv_slice.loc[:, 'name'].apply(lambda x: x + "--end")
#     # csv_slice.loc[:, '名称2'] = csv_slice.loc[:, "name"] + "sss"
