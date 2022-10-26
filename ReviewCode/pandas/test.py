import pandas as pd
import numpy as np
from tqdm import tqdm

def temp(year,name,gender,count):
    year,count=str(year),str(count)
    gender="女性" if gender=="F" else "男性"

    return f"在{year}年,叫做{name} 性别为{gender}的新生儿有{count}个"


tqdm.pandas(desc='apply')
data=pd.read_csv(r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\data.csv',encoding='utf-8')

data.progress_apply(lambda x:temp(x['year'],x['name'],x['gender'],x['count']),axis=1)