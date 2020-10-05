import pandas as pd

dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(dict_temp, index=['a', 'b', 'c', 'd'])
print(df)
print(df.index)  # RangeIndex(start=0, stop=4, step=1)
print(df.columns)  # Index(['city', 'name', 'sex', 'year'], dtype='object')

print("'name'in df.columns:", 'name' in df.columns)
print("'a'in df.index:", 'a' in df.index)

print("插入索引")
df.index.insert(0, 'w')  # 插入失败
print(df.index)
