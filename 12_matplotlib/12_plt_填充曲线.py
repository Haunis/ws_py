"""

plt.fill_between(x, 0, y, facecolor='r', alpha=0.3)
    x：第一个参数表示覆盖的区域， x，表示整个x都覆盖
    0：表示覆盖的下限;就是填充区域向上填充和向下填充的分割线
    y：表示覆盖的上限是y这个曲线
    facecolor：覆盖区域的颜色
    alpha：覆盖区域的透明度[0,1],其值越大，表示越不透明

"""
import numpy as np
import matplotlib.pyplot as plt

print("----------------1.在x轴(y=0)和y曲线之间填充----------------------")
fig = plt.figure(1)
x = np.linspace(0, 1, 500)
y = np.sin(3 * np.pi * x) * np.exp(-4 * x)
# fig, ax = plt.subplots(1, 2)
# ax[0].plot([1, 2, 3, 4])


# fig.add_subplot(1, 2, 1)
plt.subplot(1, 2, 1)  # 不使用fig.add_subplot()的话,可以使用plt.subplot()
plt.plot(x, y)

plt.fill_between(x, 0, y, facecolor='r', alpha=0.3)
plt.fill_between(x[15:300], 0, 0.4, facecolor='green', alpha=0.3)
# plt.show()

print("----------------2.在两条曲线之间填充----------------------")
# fig.add_subplot(1, 2, 2)
plt.subplot(1, 2, 2)

y2 = y - 0.2

plt.plot(x, y, color='b', label='photo1')
plt.plot(x, y2, color='r', label='photo2')

plt.fill_between(x, y, y2, facecolor='green', alpha=0.3)

plt.legend(loc='best')

plt.show()
