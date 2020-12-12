"""
在已有DataFrame的基础上创建新的DataFrame
和Series.reindex()使用类似

DataFrame.reindex(index,columns,fill_value,...)
    返回一个新的DataFrame
    参数使用说明
    index	用于索引的新序列
    method	插值（填充）方式
    fill_value	缺失值替换值
    limit	最大填充量
    level
    copy	在Multiindex的指定级别上匹配简单索引，否则选取其子集
    默认为True，无论如何都复制；如果为False，则新旧相等时就不复制

"""
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(9).reshape(3, 3),
                  index=['a', 'c', 'd'], columns=['one', 'two', 'four'])
print(df)

print("\n------------reindex----------")
df2 = df.reindex(index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three', 'four'])
print(df2)

print("\n------------fill_value----------")
df2 = df.reindex(index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three', 'four'],
                 fill_value=100)
print(df2)
