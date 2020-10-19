"""
缺失值所在的特征为数值型时，通常利用其均值、中位数和众数等描述其集中趋势的统计量来填充；
缺失值所在特征为类别型数据时，则选择众数来填充。

DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None)
    value:用于填充缺失值的标量值或字典对象
    method:	插值方式
    axis:	待填充的轴，默认axis=0
    inplace:	修改调用者对象而不产生副本
    limit:	(对于前向和后向填充)可以连续填充的最大数量

"""
import pandas as pd
import numpy as np
from numpy import nan as NA

print("--------------1.字典填充缺失值------------")
df = pd.DataFrame(np.random.randn(5, 3))
df.loc[:3, 1] = NA  # 0~3行,第1列
df.loc[:2, 2] = NA  # 0~2行,第2列
print(df, end="\n\n")
ret = df.fillna({1: 0.88, 2: 0.66})
print(ret)

print("\n--------------2.向前填充------------")
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA  # 第2行开始到最后,第1列
df.iloc[4:, 2] = NA  # 第4行开始到最后,第2列
print(df, end="\n\n")
ret = df.fillna(method='ffill')  # 就是用该列的前一个值填充
print(ret)

print("\n--------------3.series用均值填充------------")
data = pd.DataFrame([[1., 5.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 5.5, 3.]])
se = pd.Series([1., NA, 3.5, NA, 7])
ret_se = se.fillna(data.mean())
print(se, end="\n\n")
print(data.mean(), end="\n\n")
print(ret_se, end="\n\n")

print("\n--------------4.df用均值填充------------")
df = pd.DataFrame(np.arange(1, 13).reshape(4, 3))
df.iloc[2:, 1] = NA  # 第2行开始到最后,第1列
df.iloc[3:, 2] = NA  # 第三行开始到最后,第2列
print(df, end="\n\n")
df[1] = df[1].fillna(df[1].mean())
print(df)
