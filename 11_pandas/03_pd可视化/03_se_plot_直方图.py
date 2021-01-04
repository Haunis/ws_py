"""
se.plot(kind='hist', bins=3, grid=True)
    在se的最小值和最大值之间，将se分成bins=3组

本demo画出的直方图和频率分布直方图不同
    本demo：y轴是数值
    频率分布直方图：y轴是频率/组距，参考:http://www.doc88.com/p-5028405822946.html

注意和se.plot(kind='bar', rot=3)的区别：
    本demo:x是某个区间，y是这个区间的数量
    bar图：就是柱状图，表示每个index上的值

pandas中的直方图可以通过hist方法绘制
    绘制的是频数分布直方图，面积代表的是数量


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
# df.plot(kind='barh') #barh将索引放在y轴上
# plt.show()

# se = pd.Series(np.random.randint(0, high=20, size=20))
se = pd.Series([1, 2, 2, 3, 3, 3])
print("\nse:\n", se)
# se.hist(bins=3, grid=True)  # bins:分为几组, grid:是否有栅栏
se.plot(kind='hist', bins=3, grid=True)  # 最小值1到最大值3之间，分三组[1,1.66),[1.66,2.33),[2.33,3)
plt.show()
