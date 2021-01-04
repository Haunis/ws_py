"""

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y = np.sin(3 * np.pi * x) * np.exp(-4 * x)
# fig, ax = plt.subplots()
# ax.fill(x, y)
plt.subplot(1, 2, 1)
plt.fill(x, y)

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.fill_between(x, 0, y, facecolor='b', alpha=0.3)  # 和上述plt.fill()效果一样

plt.show()
