"""
set_index(keys):
    不使用默认的索引,指定columns作为索引
    set_index后,keys这一列已经不算是DataFrame的列了
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

print("\n-----------set_index-------------")
df2 = df.set_index('city')
print(df2)
print(df2.iloc[:, 0])  # set_index后,city已经不算是列里的了
