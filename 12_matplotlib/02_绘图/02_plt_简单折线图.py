"""
折线图（line chart）是一种将数据点按照顺序连接起来的图形
可以看作是将散点图，按照x轴坐标顺序连接起来的图形。

plt.plot(x,y,color,linestyle,marker,alpha)
    x，y: 接收array。表示x轴和y轴对应的数据。无默认。
    color:	接收特定string。指定线条的颜色。默认为None。
    linestyle:	接收特定string。指定线条类型。默认为“-”。
    marker:	接收特定string。表示绘制的点的类型。默认为None。
    alpha:	接收0-1的小数。表示点的透明度。默认为None。
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['SimHei']  # 配置中文显示
plt.rcParams['axes.unicode_minus'] = False

x1 = np.arange(0, 30)

plt.subplot(4, 1, 1)
plt.plot(x1, x1 * 2, 'o')  # 只画点
plt.title("只画点")

plt.subplot(4, 1, 2)
plt.plot(x1, x1 * 2)  # 只画线
plt.title("只画线")

plt.subplot(4, 1, 3)
plt.plot(x1, x1 * 2, marker='o')  # 画点和线
plt.title("画点和线")

plt.subplot(4, 1, 4)
plt.plot(x1, x1 * 2, color='r', marker='o')  # 画点和线
plt.title("画点和线,指定颜色")

plt.show()
