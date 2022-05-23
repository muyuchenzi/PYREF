import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n)
y1 = (1 - x / float(n) * np.random.uniform(0.5, 1.0, 12))
y2 = (1 - x / float(n) * np.random.uniform(0.5, 1.0, 12))

plt.bar(x, y1)
plt.bar(x, -y2)
# 显示值
for x, y in zip(x, y1):
    plt.text(x - 0.1, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(x, y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim((-0.5, 15))
plt.xticks(())
plt.ylim((-1.25, 1.25))
plt.yticks(())

plt.show()
