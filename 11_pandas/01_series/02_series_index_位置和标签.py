"""
可以使用索引的方式访问Series中的数据,如series[0]

注意事项：
    如果创建Series时指定的索引为int类型,则只能使用指定的索引访问Series中的数据
    如果创建Series时指定的索引为string类型(称之为标签)，则可以使用指定的string索引和默认0,1,2..访问Series数据

series[0]:使用位置的方式访问数据
serice["hello"]:使用标签的方式访问数据
"""

import pandas as pd

index1 = range(10, 14)
index2 = ['aa', 'bb', 'cc', 'dd']
val = [0, 1, 2, 3]

s_index_default = pd.Series(val)
s_index_int = pd.Series(val, index=index1)
s_index_str = pd.Series(val, index=index2)

print("------------1.se.index对象----------------")
print("s_index_default.index:", s_index_default.index)  # RangeIndex(start=0, stop=4, step=1)
print("s_index_int.index:", s_index_int.index)  # RangeIndex(start=10, stop=14, step=1)
print("s_index_str.index:", s_index_str.index)  # Index(['aa', 'bb', 'cc', 'dd'], dtype='object')

print("\n-----------2.访问index里的值----------------")
print("s_index_default[0]:", s_index_default[0])  # 0； 使用位置的方式访问

print("s_index_int[10]:", s_index_int[10])  # 0;已经指定了index为int,只能使用位置的方式访问
# print("s1[0]:", s1[0])  # error; 指定了int型的index,只能使用指定值访问

print("s_index_str['aa']:", s_index_str["aa"])  # 0可以用string类型的index访问--也就是使用标签访问
print('s_index_str[0]:', s_index_str[0])  # 0;也可以使用默认的0 1 2 3 访问

print("\n-----------3.修改index-------------------")
print("\nbefore ,s_index_int:\n", s_index_int)
s_index_int.index = ['aaaa', 'bbbbb', 'cccc', 'dddd']  # 修改其索引
print("\nafter ,s_index_int:\n", s_index_int)
