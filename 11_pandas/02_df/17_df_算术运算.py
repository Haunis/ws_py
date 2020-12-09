"""
 Pandas的数据对象在进行算术运算时
     相同索引进行算术运算
     不是相同索引的,则会自动进行数据对齐，但会引入缺失值

可以和Series算术运算一块看
"""
import pandas as pd
import numpy as np

a = np.arange(6).reshape(2, 3)
b = np.arange(4).reshape(2, 2)

df1 = pd.DataFrame(a, columns=['a', 'b', 'e'], index=['A', 'C'])
print('df1:\n', df1, end="\n\n")

df2 = pd.DataFrame(b, columns=['a', 'b'], index=['A', 'D'])
print('df2:\n', df2, end="\n\n")

print('df1+df2:\n', df1 + df2)
