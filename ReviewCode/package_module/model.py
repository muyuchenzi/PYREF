import c1
import c2
# from inner.inner_function import inner_var
import inner.inner_function

c1_data = c1.c1_data
c1_function = c1.c1_fuction()
print(f'c1模块的数据为{c1_data}')
print(f"c1函数的运行{c1_function}")

c2_data = c2.c2_data
print(f"导入C2模块的数据为：{c2_data}")
inner_inner_function_data = inner.inner_function.inner_var
print(f'inner 文件里 inner_function 里的数据为{inner_inner_function_data}')
