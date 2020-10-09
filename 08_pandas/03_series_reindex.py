"""
Series.reindex(list,fill_value,method)
    返回一个新的Series，如果某个索引对应的value不存在的话，则默认是NaN
    list:使用新的索引
    fill_value:使用指定的值填充
    method:对于顺序数据，比如时间序列，重新索引时可能需要进行插值或填值处理，利用参数method选项可以设置
            method = ‘ffill’或‘pad’，表示前向值填充,使用前面一个数据的value
            method = ‘bfill’或‘backfill’，表示后向值填充,使用后面一个数据的value


"""
import pandas as pd
import numpy as np

se = pd.Series([7.2, -4.3, 4.5, 3.6], index=['b', 'a', 'd', 'c'])
print("se:\n", se)

print("\n------------1.fill_value---------------")
se2 = se.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)  # se保持不变
print("se2:\n%s" % se2.__str__())

print("\n------------2.method---------------")
se1 = pd.Series(['blue', 'red', 'black'], index=[0, 2, 4])
print("se1:\n", se1, end="\n\n")
se2 = se1.reindex(np.arange(6), method='bfill')
print("se2:\n", se2)
