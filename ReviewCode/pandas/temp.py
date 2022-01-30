import numpy as np
import pandas as pd

data = {"x": 2 ** np.arange(5),
        "y": 3 ** np.arange(5),
        "z": np.array([45, 98, 24, 11, 64])}
df_1 = pd.DataFrame(data)
df = pd.DataFrame(data=data, index=[i for i in 'abcde'])
mask = df['z'] < 50

# df[mask]["z"] = 0
df[df['z'] < 50, 'z'] = 0
df.loc[mask, 'z'] = 0
df.loc[:, "t"] = 0
dt = df['x'].apply(lambda x: x * 10)
