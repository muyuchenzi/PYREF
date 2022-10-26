import pandas as pd
import numpy as np

classno = [1, 1, 1, 2, 2, 2]
student = ['张三', '李四', '王五', '刘六', '唐七', '赵八']
chinese = [70, 80, 90, 20, 30, 40]
english = [75, 85, 95, 35, 45, 55]
math = [40, 50, 60, 70, 90, 80]
physcis = [45, 55, 65, 65, 75, 85]
dict = {'班级': classno, '学生': student, '语文': chinese, '英语': english, '数学': english, '物理': physcis}
df = pd.DataFrame(dict)
df = df.set_index(['班级', '学生'])
df.columns = [['文科', '文科', '理科', '理科'], ['语文', '英语', '数学', '物理']]
df.columns.names = ['文理', '科目']
df_stacked = df.stack()
