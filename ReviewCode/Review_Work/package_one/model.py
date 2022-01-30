import c1
import c2

import inner.inner_function as import_data
from inner import *

c1_data = c1.c1_data
c1_function = c1.c1_function()
print(f'c1模块的数据为{c1_data}')
print(f"c1函数的运行{c1_function}")

c2_data = c2.c2_data
print(f"导入C2模块的数据为：{c2_data}")
inner_inner_function_data = import_data.inner_var
# print(f'inner 文件里 inner_function 里的数据为{inner_inner_function_data}')

print(inner_inner_function_data)
