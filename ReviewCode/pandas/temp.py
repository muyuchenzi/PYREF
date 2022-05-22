import pandas as pd
import numpy as np

np.random.seed(80)
df = pd.DataFrame(np.random.rand(4, 4), columns=list("ABCD"))

# 61

df['E'] = (df['C'] * df["D"] > 0.1) * 1
df["F"] = sum(df['E']) / len(df)
