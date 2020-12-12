"""
DataFrame数据查询和编辑:
    head（） #默认获取前5行
    head（n）#获取前n行
    tail（）#默认获取后5行
    head（n）#获取后n行
    sample（n）#随机抽取n行显示

    df['name'] #获取columns为'name'的这一列数据
    df[:2] #获取前两行数据

DataFrame.loc(arg1，arg2)
    arg1: 行索引名称或条件; 如 :--所有行， [1,3]--第0行和第1行
    arg2: 列索引名称，如 ['name','year']--取name和year这两列
    df.loc[[1, 3], ['name', 'year']]

DataFrame.iloc(arg1，arg2)
    arg1: 行索引位置; 如 :--所有行， [1,3]--第1行和第3行
    arg2: 列索引位置; 如 [1, 3]--第1列，第3列
    df.iloc[[1, 3], [1, 3]]
"""
import pandas as pd

dict_temp = {
    'name': ['张三0', '李四0', '王五0', '赵六0'],
    'sex': ['female1', 'female1', 'male1', 'male1'],
    'year': [2001, 2002, 2003, 2004],
    'city': ['北京3', '上海3', '广州3', '深圳3']
}

df = pd.DataFrame(dict_temp)  # DataFrame对象
print(df)

print("\n---------1.选取1列数据---------------")
se = df['name']  # 一列是Series
print(se)

print("\n---------2.选取2列数据---------------")
w2 = df[['name', 'year']]  # 多列就是DataFrame
print(w2)

print("\n---------3.选取前两行, df[:2]---------------")
# print(df[:2,]) #error,不能向numpy一样取数据,ndarray[:2, ]这样ok
# print(df[0]) #error
# print(df[0:2])#ok，也是前两行
print(df[:2])

print("\n---------4.显示2,3两行, df[1:3]---------------")
print(df[1:3])

print("\n---------5.df.head()---------------")
print(df.head())  # 默认选取前5行数据

print("\n---------6.loc---------------")
print("df.loc[:, ['name', 'year']]:")
print(df.loc[:, ['name', 'year']])  # 获取name和year两列
print("df.loc[[1, 3], ['name', 'year']]:")
print(df.loc[[1, 3], ['name', 'year']])  # 获取1和3行中的name和year两列

print("\n---------7.1 iloc之查询一列---------------")
print("df.iloc[:, 3]:")
print(df.iloc[:, 3])  # 返回Series,显示第3列

print("\n---------7.2 iloc之查询多列---------------")
print("df.iloc[:, [1, 3]]")
print(df.iloc[:, [1, 3]])  # 返回Series显示第3列

print("\n---------7.3 iloc之查询一行---------------")
print("df.iloc[0, :]")
print(df.iloc[0, :])  # 返回Series,第0行； Series的index是column

print("\n---------7.4 iloc之查询多行---------------")
print("df.iloc[[1, 3],]:")
print(df.iloc[[1, 3],])  # 显示第1和第3行,注意索引从0开始
print("df.iloc[[1, 3]]:")
print(df.iloc[[1, 3]])  # 和上面df.iloc[[1, 3],]等价

print("\n---------7.5 iloc之查询多行多列---------------")
print("df.iloc[[1, 3], [1, 3]]:")
print(df.iloc[[1, 3], [1, 3]])  # 第1和第3行,第1和第3列

print("\n---------8.布尔选择---------------")
se = df['year'] == 2001  # 返回Series
print(se, end="\n\n")
df2 = df[se]  # 选取True的那一行
print(df2)
