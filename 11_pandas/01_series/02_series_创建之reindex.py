"""
在已有Series的基础上创建新的Series

Series.reindex(list,fill_value,method): 如果某个索引对应的value不存在的话，则默认是NaN
    list: 使用新的索引
    fill_value: 使用指定的值填充
    method:对于顺序数据，比如时间序列，重新索引时可能需要进行插值或填值处理，利用参数method选项可以设置
            method = ‘ffill’或‘pad’，表示前向值填充,使用前面一个数据的value
            method = ‘bfill’或‘backfill’，表示后向值填充,使用后面一个数据的value


"""
import pandas as pd
import numpy as np

se = pd.Series([4, 3, 2, 1], index=['d', 'c', 'b', 'a'])
print("原se:\n%s" % se.__str__())

print("\n------------1.参数fill_value---------------")
se2 = se.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)  # se保持不变
print("新se2:\n%s" % se2.__str__())

print("\n------------2.参数method---------------")
se1 = pd.Series(['blue', 'red', 'black'], index=[0, 2, 4])
print("原se1:\n%s" % se1.__str__())
se2 = se1.reindex(np.arange(6), method='bfill')
print("\n新se2:\n%s" % se2.__str__())
