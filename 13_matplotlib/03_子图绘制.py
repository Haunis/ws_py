"""
绘制:AxesSubplot.plot(ndarray)
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
plt.xticks([0, 0.6, 1, 3, 4])  # x轴显示的值
plt.yticks([-1, -0.5, 0, 0.5, 1])  # y轴显示的数值
# ax1.plot([1.5, 2, 3.5, -1, 1.6])  # 绘制线性图
# ax1.plot(np.arange(0,2))  # 绘制线性图
ax1.plot(pd.Series(np.arange(0, 2)))  # 绘制线性图

ax2 = fig.add_subplot(2, 2, 2)

ax3 = fig.add_subplot(2, 2, 3)
plt.xlim(0, 20)  # 范围
plt.ylim(0, 20)  # 范围

plt.show()
