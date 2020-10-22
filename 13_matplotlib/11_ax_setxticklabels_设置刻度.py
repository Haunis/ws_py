"""
AxesSubplot.set_xticklabels()可以设置非数值型坐标
"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(30).cumsum(), color='#ff0000', linestyle='dashed', marker='o', label='one')
ax.plot(np.random.randn(30).cumsum(), color='g', linestyle='dashed', marker='+', label='two')
ax.plot(np.random.randn(30).cumsum(), color='b', linestyle='dashed', marker='v', label='three')
ax.set_xticklabels(['x0', 'x1', 'x2', 'x3', 'x4', 'x5'], rotation=30, fontsize='large')
ax.legend(loc='best')
plt.show()
