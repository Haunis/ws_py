"""
AxesSubplot.set_xticks(list) 设置x轴刻度
和plt.xticks(list)
"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
print(type(ax))
ax.plot(np.random.randn(30).cumsum(), color='#ff0000', linestyle='dashed', marker='o', label='one')
ax.plot(np.random.randn(30).cumsum(), color='g', linestyle='dashed', marker='+', label='two')
ax.plot(np.random.randn(30).cumsum(), color='b', linestyle='dashed', marker='v', label='three')
ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 40])
ax.legend(loc='best')
plt.show()
