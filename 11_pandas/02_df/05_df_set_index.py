"""
使用已有的列作为index

set_index(column):
    使用指定column作为索引
    set_index后,column这一列已经不算DataFrame的列了
"""
import pandas as pd

dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象
print(df)

print("\n-----------set_index('city')-------------")
df2 = df.set_index('city')
print(df2)
print("\ndf2.iloc[:, 0]:\n%s" % df2.iloc[:, 0].__str__())  # set_index后,city已经不算是列里的了
