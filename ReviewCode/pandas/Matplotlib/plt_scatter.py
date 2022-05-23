import matplotlib.pyplot as plt
import numpy as np

# 散点图
node_num = 1024
x = np.random.normal(0, 1, node_num)
y = np.random.normal(0, 1, node_num)
T = np.arctan2(y, x)  # color 图谱

plt.scatter(y, x, s=75, c=T, alpha=0.5)  # s=size c=color alpha 透明度
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

# 隐藏xticks
plt.xticks(())
plt.yticks(())
plt.show()
