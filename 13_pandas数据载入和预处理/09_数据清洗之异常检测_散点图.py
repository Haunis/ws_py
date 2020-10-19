"""
简单的数据统计方法中常用散点图、箱线图和3σ法则检测异常值。

散点图方法: 通过数据分布的散点图发现异常数据。
箱线图分析: 利用数据中的五个统计量（最小值、下四分位数、中位数、上四分位数和最大值）来描述数据。
3σ法则: 在3σ原则下，异常值被定义为一组测定值中与平均值的偏差超过3倍标准差的值。
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20), columns=['W'])
df['Y'] = df['W'] * 1.5 + 2  # 增加一列
df.iloc[3, 1] = 128  # 第3行,第1列元素
df.iloc[18, 1] = 150
print(df)
df.plot(kind='scatter', x='W', y='Y')
plt.show()

plt.boxplot(df['Y'].values, notch=True)
plt.show()
