import pandas as pd

dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象

print('信息表的所有值为：\n', df.values, end='\n\n')
print('信息表的所有列为：', df.columns)
print('信息表的元素个数为： ', df.size)  # 16
print('信息表的维度是: ', df.ndim)  # 2
print('信息表的形状为：', df.shape)  # (4,4)
