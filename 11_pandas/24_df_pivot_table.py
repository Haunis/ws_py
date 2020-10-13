"""
数据透视表（Pivot Table）是数据分析中常见的工具之一，根据一个或多个键值对数据进行聚合，根据列或行的分组键将数据划分到各个区域。

pivot_table(data, values=None, index=None, columns=None, aggfunc='mean',
    fill_value=None, margins=False, dropna=True, margins_name='All')

    data	接收DataFrame，表示创建表的数据
    values	接收string，指定要聚合的数据字段，默认全部数据
    index	接收string或list，表示行分组键
    columns	接收string或list，表示列分组键
    aggfunc    	接收functions，表示聚合函数，默认为mean
    margins	接收boolean，表示汇总功能的开关
    dropna	接收boolean，表示是否删掉全为NaN的列，默认False
"""

import pandas as pd

import numpy as np

data = pd.DataFrame({'k1': ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],
                     'k2': ['one', 'one', 'one', 'one', 'two', 'two', 'two', 'two', 'three', 'three', 'three', 'three'],
                     'x': np.arange(1, 13),
                     'y': np.arange(1, 13)})
print(data)  # DataFrame
print("\n--------------------1.默认aggfunc-----------------------")
ret_df = data.pivot_table(index='k1', columns='k2')  # DataFrame
print(ret_df)  # 生成的结果中k1,k2对应的值为平均值--因为默认aggfunc是mean

print("\n--------------------2.aggfunc=sum-----------------------")
ret_df = data.pivot_table(index='k1', columns='k2', aggfunc='sum')
print(ret_df)
