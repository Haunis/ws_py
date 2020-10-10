"""
sort_index：
    对索引进行排序，默认为升序，降序排序时加参数 ascending=False。
sort_values：
    对数值进行排序。by参数设置待排序的列名

和DataFrame排序对照来看
"""

import pandas as pd

se = pd.Series([1, 7, 4, 0], index=['c', 'b', 'a', 'd'])
print(se)
print('排序后的Series:\n', se.sort_index())
print('值排序后的Series:\n', se.sort_values())
