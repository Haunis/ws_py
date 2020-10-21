"""

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y1 = np.sin(3 * np.pi * x) * np.exp(-4 * x)
y2 = y1 - 0.2
plt.plot(x, y1, color='b', label='photo1')
plt.plot(x, y2, color='r', label='photo2')
plt.legend(loc='best')
plt.fill_between(x, y1, y2, facecolor='green', alpha=0.3)

plt.show()
