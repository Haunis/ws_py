"""

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
se = pd.Series([1, 2, 3, 4])  # 仅有一个数组构成; index默认从0开始
print("se:\n", se)
print("se.shape:", se.shape)  # (4,)返回元组，代表有几个元素

print("\n-----------2.使用指定索引和列表创建----------------")
i = ["i_a", "i_b", "i_c", "i_d"]
v = [1, 2, 3, 4]
se = pd.Series(v, index=i, name="col")
print(se)

print("\n-----------3.1使用字典创建Series---------------")
d_temp = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
se = pd.Series(d_temp)
print(se)

print("\n-----------3.2使用字典和指定索引创建Series--------")
d_temp = {"a": 100, "b": 200, "e": 300}
i_temp = ["a", "b", "c", "e"]

se = pd.Series(d_temp, index=i_temp)  # se形状由index决定，value到给定字典找，找不到为None
print(se)

print("\n-----------4.使用ndarray创建-------------------")
se = pd.Series(np.arange(3))
print(se)


