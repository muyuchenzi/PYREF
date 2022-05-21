import pandas as pd
import numpy as np

np.random.seed(80)
df = pd.DataFrame(np.random.rand(10, 4), columns=list("ABCD"))
