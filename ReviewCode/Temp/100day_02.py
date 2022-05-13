# 计算圆的半径周长面积

input_alpha = input("请输入圆的半径")
pi = 3.1415926

permiter = 2*pi*float(input_alpha)
area = pi*float(input_alpha)*float(input_alpha)
print(f"圆的周长为：{permiter}")
print(f"圆的面积为：{area}")
