"""

交叉表是一种特殊的透视表，主要用于计算分组频率。

    crosstab(index, columns, values=None, rownames=None,
        colnames=None, aggfunc=None, margins=False, dropna=True, normalize=False)

        index	接收 string或list，表示行索引键，无默认
        columns	接收string或list，表示列索引键
        values	接收array，表示聚合数据，默认为None
        rownames	表示行分组键名，无默认
        colnames	表示列分组键名，无默认
        aggfunc   	接收functions，表示聚合函数，默认为None
        margins	接收boolean，表示汇总功能的开关
        dropna	接收boolean，表示是否删掉全为NaN的列，默认False
        normalize	接收boolean，表示是否对值进行标准化，默认为False

"""

import pandas as pd
import numpy as np

data = pd.DataFrame({'k1': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c'],
                     'k2': ['one', 'one', 'one', 'one', 'two', 'two', 'two', 'two', 'three', 'three', 'three', 'three'],
                     'w': np.arange(1, 13),
                     'y': np.arange(1, 13)})
print(data)
print("\n-----------1.pd.crosstab()----------")
ret_df = pd.crosstab(data.k1, data.k2)  # DataFrame
print(ret_df)

print("\n-----------2.margins为True----------")
ret = pd.crosstab(data.k1, data.k2, margins=True)
print(ret)
