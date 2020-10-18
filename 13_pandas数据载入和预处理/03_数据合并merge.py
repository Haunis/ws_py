"""
参考：https://blog.csdn.net/qq_41664845/article/details/80047109

用于通过一个或多个键将两个数据集的行连接起来，类似于 SQL 中的 JOIN。
该函数的典型应用场景是，针对同一个主键存在两张包含不同字段的表，现在我们想把他们整合到一张表里。
在此典型情况下，结果集的行数并没有增加，列数则为两个元数据的列数和减去连接键的数量。

merge函数是通过一个或多个键将两个DataFrame按行合并起来

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
    left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'),
    copy=True, indicator=False, validate=None)

    left:	参与合并的左侧DataFrame
    right:	参与合并的右侧DataFrame
    how:	连接方法:inner，left，right，outer
    on:	用于连接的列名;必须存在右右两个DataFrame对象中，如果没有指定且其他参数也未指定则以两个DataFrame的列名交集做为连接键
    left_on:	左侧DataFrame中用于连接键的列
    right_on:	右侧DataFrame中用于连接键的列
    left_index:	左侧DataFrame中行索引作为连接键
    right_index:	右侧DataFrame中行索引作为连接键
    sort:	合并后会对数据排序，默认为True
    suffixes:	修改重复名;字符串值组成的元组，用于指定当左右DataFrame存在相同列名时在列名后面附加的后缀名称，默认为('_x','_y')

与SQL中的 join 用法类似,但还是有区别的：
    inner join: sql是将两个表(如a 11行，b 12行)合并成一个11*12行的大表
                而pd.merge是取key的交集
"""
import pandas as pd
import numpy as np

print("\n------------------1.默认合并--------------------\n")
df_price = pd.DataFrame({'fruit': ['a', 'b', 'c', 'd'],
                         'price': [8, 7, 9, 11]})
df_amount = pd.DataFrame({'fruit': ['a', 'b', 'c'],
                          'amount': [5, 11, 8]})
# display(df_price, amount, pd.merge(df_price, amount))
# 没有指定连接键，默认用重叠列名(就是fruit)
# 将第二个DataFrame df_amount的列放在第一个df的列的后面
ret_def = pd.merge(df_price, df_amount, on='fruit', how="inner")  # 默认inner join,取key交集,d没有链接上
# ret_def = pd.merge(df_price, df_amount, how="inner")  # 默认inner join,取key交集,d没有链接上
print("df_price:")
print(df_price, end="\n\n")

print('df_amount:')
print(df_amount, end="\n\n")

print("ret_def:")
print(ret_def, end="\n\n")

print("\n------------------2.指定合并时的列名--------------------\n")
# 如果两个对象的列名不同可以分别指定
# ret_def = pd.merge(df_price, df_amount, left_on='fruit', right_on='fruit')
ret_def = pd.merge(df_price, df_amount, left_on='price', right_on='amount')
print(ret_def)

print("\n------------------3.通过多个键合并--------------------\n")
# 就是两列名字都相等时才链接
left = pd.DataFrame({'key1': ['one', 'one', 'two'], 'key2': ['a', 'b', 'a'], 'value1': np.arange(1, 4)})
right = pd.DataFrame({'key1': ['one', 'one', 'two', 'two'], 'key2': ['a', 'a', 'a', 'b'], 'value2': np.arange(11, 15)})
df = pd.merge(left, right, on=['key1', 'key2'], how='left')
# df = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(left, end="\n\n")
print(right, end="\n\n")
print(df, end="\n\n")

print("\n------------------4.suffixes的应用--------------------\n")
# 该合并会产生的df比不指定on时合并的df更大
# suffixes 就是合并时，列名重复时，给列名取别名
print(pd.merge(left, right, on='key1', how="inner"))  # 默认how=inner,就是取key交集
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))
