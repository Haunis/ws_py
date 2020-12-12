import pandas as pd

dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象
print(df)

print('信息表的所有值为：\n', df.values, end='\n\n')  # ndarray

print('信息表的所有列为：', df.columns)  # df.columns为Index对象
print('信息表的元素个数为： ', df.size)  # 16; 行*列
print('信息表的维度是: ', df.ndim)  # 2
print('信息表的形状为：', df.shape)  # (4,4)

print("------------1.df重新设定columns--------------")
df.columns = ['c0', 'c1', 'c2', 'c3']
print(df)

print("------------2.df重新设定columns--------------")
df.index = ['i0', 'i1', 'i2', 'i3']
print(df)