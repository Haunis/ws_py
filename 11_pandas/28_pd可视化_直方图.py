"""
直方图用于频率分布，y轴为数值或比率。绘制直方图，可以观察数据值的大致分布规律
pandas中的直方图可以通过hist方法绘制

核密度估计是对真实密度的估计，其过程是将数据的分布近似为一组核（如正态分布）
通过plot函数的kind = ‘kde’可以进行绘制。

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)),
                  index={'one', 'two', 'three'},
                  columns=['I1', 'I2', 'I3'])
print(df)
# df.plot(kind='barh')
# plt.show()

# se = pd.Series(np.random.randint(0, high=20, size=20))
se = pd.Series([1,2,2,3,3,3])
print(se)
se.hist(bins=3, grid=True)  # bins:分为几组, grid:是否有栅栏
plt.show()
