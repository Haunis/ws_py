"""


"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y = np.sin(3 * np.pi * x) * np.exp(-4 * x)
fig, ax = plt.subplots()
plt.plot(x, y)

# x：第一个参数表示覆盖的区域， x，表示整个x都覆盖
# 0：表示覆盖的下限;就是填充区域向上填充和向下填充的分割线
# y：表示覆盖的上限是y这个曲线
# facecolor：覆盖区域的颜色
# alpha：覆盖区域的透明度[0,1],其值越大，表示越不透明

plt.fill_between(x, 0, y, facecolor='r', alpha=0.3)
plt.fill_between(x[15:300], 0, 0.4, facecolor = 'green', alpha = 0.3)
plt.show()
