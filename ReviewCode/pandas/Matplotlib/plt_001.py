import matplotlib as plt
import numpy as np
from matplotlib import pyplot

x = np.linspace(-1, 1, 50)
y = 2 * x + 1
z = x ** 2
print(y)
pyplot.figure()
pyplot.plot(x, y)
pyplot.plot(x, z)
pyplot.show()

pyplot.figure(num=3, figsize=(8, 5))
pyplot.plot(x, z, color='green')
pyplot.show()
