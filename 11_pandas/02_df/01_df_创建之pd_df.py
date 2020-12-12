"""
 DataFrame
    是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）。
    既有行索引也有列索引，它可以被看做由Series组成的字典（共用同一个索引）
    和数据库的表很相似

pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
    data: 数据,可以是字典,字典的key作为字段名(行),value作为记录(列的值)
    columns: 列的名字,相当于数据库表的字段;数据可以和data的key不一致,以columns为准,data没有对应的则为NaN
    index: 长度必须和字典data长度一致,否则报错

"""
import pandas as pd
import numpy as np

print("\n-------------1.使用字典创建DataFrame--------------")
dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象
print(df)

print("\n-------------2.使用字典和指定columns创建---------------")
# 以指定的columns为准，字典中有的则列出来，无则为NaN
# dict_temp没有'temp_field'这个key,temp_field在DataFrame这一列对应的value为NaN
df1 = pd.DataFrame(dict_temp, columns=['name', 'year', 'sex', 'city', 'temp_field'])
print(df1)

print("\n-------------3.使用字典和指定columns,index创建---------------")
df3 = pd.DataFrame(dict_temp, columns=['name', 'sex', 'year', 'city'],
                   index=['a', 'b', 'c', 'd'])
print(df3)

print("\n-------------4.使用ndarray和指定columns,index创建---------------")
df4 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   index=['a', 'c', 'd'], columns=['one', 'two', 'four'])
print(df4)
