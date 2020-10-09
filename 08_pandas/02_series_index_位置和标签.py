"""
可以使用索引的方式访问Series中的数据,如series[0]
    如果创建Series时指定的索引为int类型,则只能使用指定的索引访问Series中的数据
    如果创建Series时指定的索引为string类型(称之为标签)
        则可以使用指定的string索引和默认0 1 2 访问Series数据
series[0]:使用位置的方式访问数据
serice["hello"]:使用标签的方式访问数据
"""

import pandas as pd

index1 = range(10, 14)
index2 = "hello the cruel world".split()
val = [0, 1, 2, 3]

s0 = pd.Series(val)
s1 = pd.Series(val, index=index1)
s2 = pd.Series(val, index=index2)

print("s0.index:", s0.index)  # RangeIndex对象
print("s1.index:", s1.index)  # RangeIndex对象
print("s2.index:", s2.index)  # Index对象

print("s0[0]:", s0[0])  # 位置
print("s1[10]:", s1[10])
# print("s1[0]:", s1[0])  # error; 指定了int型的index,只能使用指定值访问
print("s2['hello']:", s2["hello"])  # 可以用string类型的index访问--也就是使用标签访问
print('s2[0]:', s2[0])  # 也可以使用默认的0 1 2 3 访问
