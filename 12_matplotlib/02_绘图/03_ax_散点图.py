"""
散点图（scatter diagram）又称为散点分布图,是以一个特征为横坐标,
另一个特征为纵坐标，利用坐标点（散点）的分布形态反映特征间的统计关系的一种图形

ax.scatter(x,y,c,s,linewidths,marker,alpha)
    x，y:接收array。表示x轴和y轴对应的数据。无默认。
    c: 接收颜色或者一维的array。指定点的颜色，若传入一维array则表示每个点的颜色。默认为None
    s: 接收数值或者一维的array。
        构成的点是由圆环构成,圆环线的宽度
        指定点的大小，若传入一维array则表示每个点的大小。默认为None。

    linewidths:点的大小.
    marker:接收特定string。表示绘制的点的类型。默认为None。
    alpha:接收0-1的小数。表示点的透明度。默认为None。
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

plt.figure(figsize=(20, 5))
# fig, ax = plt.subplots()

print('-----------1.第1个图---------------')

ax = plt.subplot(1, 3, 1)  # AxesSubplot
plt.title('1st: 散点图')
plt.xlabel('X')
plt.ylabel('Y')
plt.tick_params(labelsize=16)

x = np.arange(0, 10 * np.pi, 0.4)
y = np.sin(x)
ax.plot(x, y)  # 曲线
ax.scatter(x, y, c='r', label="red", s=100, linewidths=x, marker='o', alpha=0.8)  # 散点图
# ax.scatter(x, y + 0.3, c='g', label="green", s=100, linewidths=x, marker='o', alpha=0.9, edgecolors='face')  # 散点图
plt.legend(['折线', '散点'], loc='lower left')

print('-----------2.第2个图---------------')
ax = plt.subplot(1, 3, 2)  # AxesSubplot
plt.title("2st: s linewidths param")
plt.xlim(0, 20)  # 范围
plt.ylim(0, 20)  # 范围
plt.tick_params(labelsize=16)
ax.scatter(5, 5, c='r', s=50, linewidths=100, marker='o')  # 散点图
ax.scatter(15, 5, c='g', s=500, linewidths=100, marker='o')  # 散点图

print('-----------3.第3个图---------------')
ax = plt.subplot(1, 3, 3)  # AxesSubplot
plt.title("3st： random")
plt.tick_params(labelsize=16)
for color in ['red', 'green', 'blue']:
    n = 500
    x, y = np.random.randn(2, n)  # 返回ndarray,然后拆包成两行 x,y
    ax.scatter(x, y, c=color, label=color, alpha=0.3)
    ax.legend()
    ax.grid(True)

plt.show()
