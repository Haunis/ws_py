"""
Pandas（Python Data Analysis Library）是基于NumPy的数据分析模块，
    它提供了大量标准数据模型和高效操作大型数据集所需的工具
    可以说Pandas是使得Python能够成为高效且强大的数据分析环境的重要因素之一。

Pandas有三种数据结构：Series、DataFrame和Panel。
    Series类似于一维数组；
    DataFrame是类似表格的二维数组；
    Panel可以视为Excel的多表单Sheet

Series的创建:
    pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
    返回<class 'pandas.core.series.Series'>对象
    参数说明:
        data: 可以是列表,也可以是字典
        index:可以指定;不指定的话,默认从0开始
              如果data是列表的话,指定index的长度和列表的长度必须相同
              如果data是字典的话,指定index的长度可以不和字典长度一致;
                    以index为准,字典有对应value的则取该value; 字典无该value则index对应的value为NaN

Series相加:
    index相并,对应的value值相加

"""
import pandas as pd
import numpy as np

print("-------------1.使用列表创建----------------")
se = pd.Series([1, -2, 3, -4])  # 仅有一个数组构成; index默认从0开始
print(se)
print(se.shape)  # (4,)返回元组，代表有几个元素

print("\n-----------2.使用指定索引和列表创建----------------")
i = ["a", "c", "d", "a"]
v = [2, 4, 5, 7]
se = pd.Series(v, index=i, name="col")
print(se)

print("\n-----------3.1使用字典创建Series---------------")
d_temp = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
se = pd.Series(d_temp)
print(se)

print("\n-----------3.2使用字典和指定索引创建Series--------")
d_temp = {"a": 100, "b": 200, "e": 300}
i_temp = ["a", "b", "c", "e"]
# 使用给定的索引到字典里找,找不到的,value置为NaN
se = pd.Series(d_temp, index=i_temp)
print(se)

print("\n-----------3.3Series相加-------------------")
d_temp = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
se1 = pd.Series(d_temp)
i_temp = ['x', 'a', 'c', 'b']
se2 = pd.Series(d_temp, index=i_temp)
print("se1:")
print(se1)
print("se2:")
print(se2)
print("se1+se2:")
print(se1 + se2)

print("\n-----------4.使用ndarray创建-------------------")
se = pd.Series(np.arange(10))
print(se)

print("\n-----------5.索引修改-------------------")
se = pd.Series([4, 7, -3, 2])  # se默认索引0 1 2 3...
se.index = ['a', 'b', 'c', 'd']  # 修改其索引
print(se)
