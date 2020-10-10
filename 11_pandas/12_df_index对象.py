"""
构建Series或 DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一个Index对象

Index对象常用方法和属性:
    append	连接另一个Index对象，产生一个新的Index
    diff	计算差集，并得到一个Index
    intersection	计算交集
    union	计算并集
    isin	计算一个指示各值是否都包含在参数集合中的布尔型数组
    delete	删除索引i处的元素，并得到新的Index
    drop	删除传入的值，并得到新的Index
    insert	将元素插入到索引i处，并得到新的Index
    is_monotonic	当各元素均大于等于前一个元素时，返回True
    is.unique	当Index没有重复值时，返回True
    unique	计算Index中唯一值的数组
"""

import pandas as pd

dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(dict_temp, index=['a', 'b', 'c', 'd'])

print(df)
print("df.index: ", df.index)  # Index对象; 如果不指定index就是RangeIndex对象
print("df.columns:", df.columns)  # Index(['city', 'name', 'sex', 'year'], dtype='object')

print()
print("'name'in df.columns:", 'name' in df.columns)  # True
print("'a'in df.index:", 'a' in df.index)  # True

print("\n--------index.insert()------")
df.index.insert(0, 'w')  # 插入失败
print(df.index)
