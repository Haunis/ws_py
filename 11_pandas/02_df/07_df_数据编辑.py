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
    'name': ['张三0', '李四0', '王五0', '赵六0'],
    'sex': ['female1', 'female1', 'male1', 'male1'],
    'year': [2001, 2002, 2003, 2004],
    'city': ['北京3', '上海3', '广州3', '深圳3']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象
# df = df.set_index('city')  # 返回一个新的df
print(df)

print("\n--------------1.append添加一行----------------")
dict_one = {'city': '兰州', 'name': '李红', 'year': 2005, 'sex': 'female'}
df2 = df.append(dict_one, ignore_index=True)
print(df2)

print("\n--------------2.insert插入一列----------------")
df2['score'] = [0, 10, 20, 30, 40]  # 直接为列赋值
df2.insert(1, 'No', ['000', '001', '002', '003', '004'])  # 使用insert方法
print(df2)

print("\n--------------3.删除一行----------------")
# df2.drop(4)  # 返回新df
df2.drop(4, inplace=True)  # 在原来的df中删除，不返回新的df
print(df2)

print("\n--------------4.删除一列----------------")
df2.drop('score', axis=1, inplace=True)
print(df2)

print("\n--------------5.修改数据----------------")
df2['No'] = [0, 111, 222, 333]
print(df2)
