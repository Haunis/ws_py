"""
在缺失值的处理方法中，删除缺失值是常用的方法之一。通过dropna方法可以删除具有缺失值的行。

dropna(axis=0, how=‘any’, thresh=None, subset=None,  inplace=False)
    axis:默认为axis=0，当某行出现缺失值时，将该行丢弃并返回，
        当axis=1，当某列出现缺失值时，将该列丢弃
    how:表示删除的形式。
        any--只要有缺失值存在就执行删除操作;默认为any
        all--当且仅当全部为缺失值时执行删除操作
    thresh	阈值设定，当行列中非空值大于等于给定值才舍弃
    subset:表示进行去重的列∕行，如：subset=[ ’a’ ,’d’], 即丢弃子列 a d 中含有缺失值的行
    inplace:bool取值，默认False, 当inplace= True，即对原数据操作，无返回值

"""
import pandas as pd
import numpy as np
from numpy import nan as NA

print("---------------1.se.dropna()----------------\n")
se = pd.Series([1, NA, 3.5, NA, 7])
print(se, end="\n\n")
print(se.dropna())

print("\n--------------2.se[bool_se]----------------\n")
# 布尔型索引选择过滤非缺失值
not_null = se.notnull()
print(type(not_null))
print(not_null)
print(se[not_null])

print("\n--------------3.df.dropna()----------------\n")
data = pd.DataFrame([[1., 5.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 5.5, 3.]])
print(data)
cleaned = data.dropna()
print('删除缺失值后的：\n', cleaned)

print("\n--------------4.df.dropna(how='all')----------------\n")
data = pd.DataFrame([[1., 5.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 5.5, 3.]])
print(data)
ret = data.dropna(how='all')  # how='all',全部缺失才删除
print(ret)

print("\n--------------5.df.dropna(axis=1,how='all')----------------\n")
data = pd.DataFrame([[1., 5.5, NA],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 5.5, NA]])
ret = data.dropna(axis=1, how='all')
print(ret)

print("\n--------------6.df.dropna(thresh)----------------\n")
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA  # 0~4行,第1列
df.iloc[:2, 2] = NA  # 0~2行,第2列
print(df, end="\n\n")
ret = df.dropna(thresh=2)  # 当某行出现NaN大于等于2时才将该行删除
print(ret)
