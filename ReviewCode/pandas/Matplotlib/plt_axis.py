# import matplotlib as plt
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure(num=4)
line_one, = plt.plot(x, y2, label="one")
# plt线的颜色，宽度，样式
line_two, = plt.plot(x, y1, color="red", linewidth=2, linestyle='--', label='two')
# ply的xy轴的范围，名称,间距
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.ylabel("y val")
plt.xlabel('x val')

new_ticks = np.linspace(-1, 3, 10)
plt.xticks(new_ticks)
# y_ticks = ()
plt.yticks([-2, -1, 0, 1, 2, 3], ['bad', 'a', 'b', 'c', 'd', 'good'])

ax = plt.gca()
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")

# 图例
plt.legend(handles=[line_one, line_two, ], labels=['aaa', 'bbb'], loc='best')

plt.show()
