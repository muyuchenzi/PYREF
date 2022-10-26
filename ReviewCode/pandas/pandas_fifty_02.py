import pandas as pd
import numpy as np

# 23. 有一列整数列A的DatraFrame，删除数值重复的行
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7],
                   'B': [1, 2, 2, 3, 4, 5, 5, 5, 6, 9, 7]})
temp = df.drop_duplicates(subset=['A', 'B'])

# 24. 一个全数值DataFrame，每个数字减去该行的平均数

df = pd.DataFrame(np.random.random(size=(5, 3)), columns=[i for i in 'abc'])
res = pd.DataFrame(df.mean(axis=1)).rename(columns={0: 'd'})
result = pd.concat([df, res], axis=1)

result['a'] = result['a'] - result['d']
for col in result.columns:
    print(col)
    result[col] = result[col] - result['d']
# 25. 一个有3列的DataFrame，求哪一列的和最小
df.sum(axis=0).idxmin()

# 26. 给定DataFrame，求A列每个值的前3大的B的值的和
df = pd.DataFrame({'A': list('aaabbcaabcccbbc'),
                   'B': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})


def find_nlargest_three(df):
    key_val = df['A'].value_counts()
    a_value_list = list(key_val.index)
    dict_res = {}
    for i in a_value_list:
        result = df.loc[df["A"] == i].nlargest(3, columns="B").reset_index(drop=True)
        dict_res[i] = result['B'].sum()
    return pd.DataFrame(dict_res, index=[0]).T


final_result = find_nlargest_three(df=df)

# 27. 给定DataFrame，有列A, B，A的值在1-100（含），对A列每10步长，求对应的B的和
df = pd.DataFrame({'A': [1, 2, 11, 11, 33, 34, 35, 40, 79, 99],
                   'B': [1, 2, 11, 11, 33, 34, 35, 40, 79, 99]})

df1 = df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()


def twenty_seven(df):
    list_val = [i * 10 for i in range(11)]
    df_columns = df.columns.to_list()
    dict_val = {}
    for li in range(len(list_val) - 1):
        for col in df_columns:
            res = df.loc[(df[col] > list_val[li]) & (df[col] < list_val[li + 1])]
            res_sum = sum(res[col])
            dict_val[str(list_val[li]) + "_" + str(list_val[li + 1])] = res_sum

    result = pd.DataFrame(dict_val, index=[0]).T
    return result


twenty_seven(df)

# 28. 给定DataFrame，计算每个元素至左边最近的0（或者至开头）的距离，生成新列y NOTE这个不需要搞
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

izero = np.r_[-1, (df['X'] == 0).to_numpy().nonzero()[0]]  # 标记0的位置
idx = np.arange(len(df))
df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]

# 29. 一个全数值的DataFrame，返回最大3个值的坐标
df = pd.DataFrame(np.random.randint(1, 100, size=(5, 5)))
aa = df.unstack().sort_values()[-3:]
aa.index.to_list()

# 30. 给定DataFrame，将负值代替为同组的平均值
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                   'vals': [-12, 345, 3, 1, 45, 14, 4, -52, 54, 23, -235, 21, 57, 3, 87]})
df_1 = df[df['vals'] > 0]
df_mean = df_1.groupby('grps')['vals'].mean()
res = dict(df_mean)
a = 1
xx = dict(a)

df_2 = df[df['vals'] <= 0]
df_2.reset_index(drop=True, inplace=True)
df_2['vals'] = df_2['grps'].apply(lambda x: res.get(x))
