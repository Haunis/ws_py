"""
箱线图利用数据中的五个统计量（最小值、下四分位数、中位数、上四分位数和最大值）来描述数据，
它也可以粗略地看出数据是否具有对称性、分布的分散程度等信息
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20), columns=['W'])
df['Y'] = df['W'] * 1.5 + 2  # 增加一列
df.iloc[3, 1] = 128  # 第3行,第1列元素
df.iloc[18, 1] = 150
print(df)

plt.boxplot(df['Y'].values, notch=True)
plt.show()
