import pandas as pd
import numpy as np
import random

series_alpha = pd.Series(index=[np.array([1, 2, 34])], data=[random.random() for i in range(3)],
                         name='sx')

xx = [random.random() for _ in range(3)]


