"""
Pandas（Python Data Analysis Library）是基于NumPy的数据分析模块，
    它提供了大量标准数据模型和高效操作大型数据集所需的工具
    可以说Pandas是使得Python能够成为高效且强大的数据分析环境的重要因素之一。

Pandas有三种数据结构：Series、DataFrame和Panel。
    Series类似于一维数组；
    DataFrame是类似表格的二维数组；
    Panel可以视为Excel的多表单Sheet

Series:
    pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
    返回<class 'pandas.core.series.Series'>对象


"""
import pandas as pd

print("-------------1.使用默认索引----------------")
se = pd.Series([1, -2, 3, -4])  # 仅有一个数组构成
print(se)

print("\n-----------2.指定索引和value----------------")
i = ["a", "c", "d", "a"]
v = [2, 4, 5, 7]
se = pd.Series(v, index=i, name="col")
print(se)
