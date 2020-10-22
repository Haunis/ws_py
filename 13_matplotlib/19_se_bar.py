"""
直方图（Histogram）又称质量分布图，是统计报告图的一种
由一系列高度不等的纵向条纹或线段表示数据分布的情况，一般用横轴表示数据所属类别，纵轴表示数量或者占比。

用直方图可以比较直观地看出产品质量特性的分布状态，便于判断其总体质量分布情况
直方图可以发现分布表无法发现的数据模式、样本的频率分布和总体的分布
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
se = pd.Series(np.linspace(-8, 8, 16), index=list('abcdefghijklmnop'))
se.plot.bar(ax=axes[0], color='b', alpha=0.7)  # 垂直柱状图
se.plot.barh(ax=axes[1], color='k', alpha=0.7)  # alpha设置透明度
plt.show()

