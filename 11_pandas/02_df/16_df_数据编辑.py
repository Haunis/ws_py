"""
添加一行:append

添加一列:insert 或者直接赋值

删除数据:drop
    删除数据直接用drop方法，通过axis参数确定是删除的是行还是列。
    默认数据删除不修改原数据，需要在原数据删除行列需要设置参数inplace = True

修改数据:直接赋值即可
    如: df['No'] = [111, 222, 333]
"""

import pandas as pd

dict_temp = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象
df = df.set_index('city')  # 返回一个新的df,原df不变,所以要重新赋值
print(df)

print("\n--------------1.append添加一行----------------")
data1 = {'city': '兰州', 'name': '李红', 'year': 2005, 'sex': 'female'}
df2 = df.append(data1, ignore_index=True)
print(df2)

print("\n--------------2.insert插入一列----------------")
df['score'] = [85, 78, 96, 80]  # 直接为列赋值
df.insert(1, 'No', ['001', '002', '003', '004'])  # 使用insert方法
print(df)

print("\n--------------3.删除一行----------------")
# df.drop("广州")  # 返回新df
df.drop("广州", inplace=True)
print(df)

print("\n--------------4.删除一列----------------")
df.drop('sex', axis=1, inplace=True)
print(df)

print("\n--------------5.修改数据----------------")
df['No'] = [111, 222, 333]
print(df)
