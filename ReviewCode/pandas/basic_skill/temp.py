import numpy as np
import pandas as pd

# 根据多个字典序列创建DataFrame

dict_alpha={
        "a":[1,2,3,4,4],
        "b":'abced',
        "str_ing":[False,True,False,False,False],
        "np":[np.nan,np.nan,np.nan,np.nan,np.nan],
        "nps":np.arange(0,5)
}
s=pd.Series(dict_alpha)
print(s)
df=pd.DataFrame(dict_alpha)
# print(df.dtypes)
# print(df.describe())
print(df[['a','np']])
print(df[['a']])
print(df.loc[:,'a'])