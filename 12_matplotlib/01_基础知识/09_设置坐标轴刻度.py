"""
指定坐标轴的刻度和标签

设置x轴刻度:
    AxesSubplot.set_xticks(ticks = [0, 5, 10, 15, 20, 25, 30, 40])

设置x轴标签:
    方式1:
        AxesSubplot.set_xticks(ticks = [0, 5, 10, 15, 20, 25, 30, 40])
        AxesSubplot.set_xticklabels(labels = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh'])
    方式2：
        plt.xticks(ticks=ticks, labels=labels)
"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
nda = np.random.randn(30).cumsum()
ticks = [0, 5, 10, 15, 20, 25, 30, 40]  # 用户绘制x轴刻度
labels = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh']  # 将x轴刻度用该标签表示

print("------------1.ax.set_xticks()----------------")
ax = fig.add_subplot(3, 1, 1)  # AxesSubplot
plt.title("ax.set_xticks()")
ax.plot(nda, color='r', linestyle='dashed', marker='o', label='one111')
ax.set_xticks(ticks)
plt.legend(loc='best')  # 将label='one111'放到最好的位置

print("------------2.ax.set_xticklabels()----------------")
ax = fig.add_subplot(3, 1, 2)
plt.title("ax.set_xticklabels()")
plt.plot(nda, color='#00ff00', linestyle='dashed', marker='+', label='two')
ax.set_xticks(ticks)  # 要加入这行,否则ax.set_xticklabels()会有warning提示
ax.set_xticklabels(labels, rotation=30, fontsize='large')
plt.legend(loc='best')

print("------------3.plt.xticks()----------------")
ax = fig.add_subplot(3, 1, 3)
plt.title("plt.xticks()")

ax.plot(nda, color='b', linestyle='dashed', marker='v', label='nda')
plt.plot(nda + 1, color='k', linestyle=':', marker='v', label='nda+1')

# ax.xticks(ticks=ticks, labels=labels)  # error;AxesSubplot无 xticks()方法
plt.xticks(ticks=ticks, labels=labels)
plt.legend(loc='best')

plt.show()
