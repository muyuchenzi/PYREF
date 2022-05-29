import sklearn
from sklearn import datasets
import pandas as pd
import numpy as np

price_data = datasets.load_boston()

iris_data = pd.DataFrame(datasets.load_iris().data)
iris_target = pd.DataFrame(datasets.load_iris().target)
