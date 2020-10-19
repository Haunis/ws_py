"""
 Pandas的数据对象在进行算术运算时
     相同索引进行算术运算
     不是相同索引的,则会自动进行数据对齐，但会引入缺失值

可以和DataFrame算术运算一块看
"""
import pandas as pd
import numpy as np

se1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

print('se1:\n%s' % se1.__str__(), end="\n\n")

se2 = pd.Series([10, 20, 30, 40], index=['d', 'e', 'f', 'g'])
print('se2:\n%s' % se2.__str__(), end="\n\n")

print(se1 + se2, end="\n\n")

print(se1.mean() > se1)  # 返回bool类型的Series
