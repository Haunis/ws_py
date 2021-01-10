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

fig, ax = plt.subplots()

x = np.arange(0, 10 * np.pi, 0.4)
y = np.sin(x)
ax = plt.subplot(1, 1, 1)  # AxesSubplot
plt.title('散点图')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['折线', '散点'], loc='lower left')

ax.plot(x, y)  # 曲线
ax.scatter(x, y, c='r', s=100, linewidths=x, marker='o')  # 散点图

# plt.ylim(0, 20)  # 范围
# plt.ylim(0, 20)  # 范围
# ax.scatter(5, 5, c='r', s=2, linewidths=100, marker='o')  # 散点图
# ax.scatter(20, 5, c='g', s=4000, linewidths=100, marker='o')  # 散点图


plt.show()
