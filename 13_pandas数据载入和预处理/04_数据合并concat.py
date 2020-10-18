"""
如果要合并的DataFrame之间没有连接键，就无法使用merge方法。
pandas中的concat方法可以实现，默认情况下会按行的方向堆叠数据。

concat连接series:
    直接将series的index和values 分别append

concat连接DataFrame:
    columns相同的，则index直接append
    columns不同的，则column横向append,不存在的元素置为NaN

"""
import pandas as pd
import numpy as np

print("--------------1.series连接--------------")
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['a', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(s1, end="\n\n")
print(s2, end="\n\n")
print(s2, end="\n\n")
print(pd.concat([s1, s2, s3]))  # Series行合并

print("--------------2.DataFrame连接--------------\n")
data1 = pd.DataFrame(np.arange(6).reshape(2, 3), columns=list('abc'))
data2 = pd.DataFrame(np.arange(20, 26).reshape(2, 3), columns=list('ayz'))
data = pd.concat([data1, data2], axis=0, sort=False)
print(data1, end="\n\n")
print(data2, end="\n\n")
print(data, end="\n\n")

print("\n-------------3.指定索引顺序--------------\n")
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['a', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
s4 = pd.concat([s1 * 5, s3], sort=False)
df5 = pd.concat([s1, s4], axis=1, sort=False)  # 将Series和DataFrame 连接
df6 = pd.concat([s1, s4], axis=1, join='inner', sort=False)
print(s4, end="\n\n")
print(df5, end="\n\n")
print(df6, end="\n\n")
