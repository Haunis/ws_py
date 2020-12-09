"""
DataFrame数据查询和编辑:
    head（） #默认获取前5行
    head（n）#获取前n行
    tail（）#默认获取后5行
    head（n）#获取后n行
    sample（n）#随机抽取n行显示

    df['name'] #获取columns为'name'的这一列数据
    df[:2] #获取前两行数据

DataFrame.loc(行索引名称或条件，列索引名称)
DataFrame.iloc(行索引位置，列索引位置)
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

print("\n---------1.选取1列数据---------------")
w1 = df['name']  # 一列是Series
print(w1)

print("\n---------2.选取2列数据---------------")
w2 = df[['name', 'year']]  # 多列就是DataFrame
print(w2)

print("\n---------3.选取前两行---------------")
print(df[:2])

print("\n---------4.显示2,3两行---------------")
print(df[1:3])

print("\n---------5.df.head()---------------")
print(df.head())

print("\n---------6.loc---------------")
df2 = df.set_index('city')  # 将'city'作为索引,这样下面的df2.loc[]指定行才会有效
print(df2.loc[:, ['name', 'year']])  # 获取name和year两列
print(df2.loc[['北京', '上海'], ['name', 'year']])  # 获取北京和上海行中的name和year两列

print("\n---------7.iloc---------------")
print(df2)
print("\n---df2.iloc[:, 2]:---")
print(df2.iloc[:, 2])  # 显示第2列;set_index后,city已经不算是列里的了

print("\n---df2.iloc[[1, 3]]:---")
print(df2.iloc[[1, 3]])  # 显示第1和第3行,注意索引从0开始

print("\n---df2.iloc[[1, 3], [1, 2]]:---")
print(df2.iloc[[1, 3], [1, 2]])  # 第1和第3行,第1和第2列

print("\n---------8.布尔选择---------------")
se = df2['year'] == 2001  # 返回Series
print(se, end="\n\n")
df3 = df2[se]
print(df3)
