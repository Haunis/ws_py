"""
核密度估计是对真实密度的估计，其过程是将数据的分布近似为一组核（如正态分布）。
通过plot函数的kind = ‘kde’可以进行绘制
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# se = pd.Series(np.random.normal(size=8))
se = pd.Series(np.arange(0, 10))
print(se)
# se.plot.kde()
se.plot(kind='kde')

# se.hist()
se.plot(kind='hist', grid=True)
# se.plot.bar( color='r', alpha=0.7)

plt.xticks(np.arange(0, 11))
plt.show()
