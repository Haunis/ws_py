"""
和数据库中的表分组很像
    对某一列A进行按某一列B进行分组： df[A].groupby(df[B])
    对所有列按某一列B进行分组： df.groupby(B)
    对df索引按字典进行分组： df.groupby(dict)

groupby方法
    根据索引或字段对数据进行分组。
    DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True,
    group_keys=True, squeeze=False, **kwargs)
        返回SeriesGroupBy对象
            by: 可以是函数、字典、Series等，用于确定分组的依据
            axis: 接收int，表示操作的轴方向，默认为0
            level: 接收int或索引名，代表标签所在级别，默认为None
            as_index: 接收boolean，表示聚合后的标签是否以DataFrame索引输出
            sort: 接收boolean，表示对分组依据和分组标签排序，默认为True
            group_keys: 接收boolean，表示是否显示分组标签的名称，默认为True
            squeeze: 接收boolean，表示是否在允许情况下对返回数据降维，默认False

SeriesGroupBy支持函数:
    count(): 计数
    sum():	求和
    mean():	求平均值
    median(): 求中位数
    std(),var(): 无偏标准差和方差
    min(),max(): 求最小值最大值
    prod():	求积
    first(),last():	第一个和最后一个值

"""
import numpy as np
import pandas as pd

dict_data = {
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['yes', 'no', 'yes', 'yes', 'no'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(dict_data)
print(df, end="\n\n")

print("\n------------1.df['data1'].groupby(df['key2'])-----------------")
# 相当于df.groupby('yyy')只取了xxx这列
se_groupby = df['data1'].groupby(df['key2'])  # 返回SeriesGroupBy; df['data1']得到的是Series
print("se_groupby.mean():")
print(se_groupby.mean(), end="\n\n")  # grouped.mean()得到的是Series

print("se_groupby.size():")
print(se_groupby.size(), end="\n\n")  # grouped.size()得到的是Series

print("se_groupby.sum():")
print(se_groupby.sum(), end="\n\n")

print("\n------------2.1 df.groupby('key2')按列分组-----------------")
# DataFrame的列作为分组键，但需要注意的是用于分组的对象必须是DataFrame数据本身，否则搜索不到索引名称会报错。
print("\ndf.groupby('key2').mean()['data1']:\n", df.groupby("key2").mean()['data1'])
print("\ndf.groupby('key2')['data1'].mean():\n", df.groupby("key2")['data1'].mean())  # 和上述相同

ret_df_groupby = df.groupby('key2')  # DataFrameGroupBy
df_key2_mean = ret_df_groupby.mean()  # df_key2_mean是DataFrame
print("\ndf_key2_mean:")
print(df_key2_mean.applymap(lambda x: "%.2f" % x))

print("\n------------2.2 df.groupby('xxx','yyy')按列分组-----------------")
df_key1_key2_mean = df.groupby(['key1', 'key2']).mean()
print(df_key1_key2_mean)

print("\n------------2.3 df.groupby(dict)按指定字典分组-----------------")
# 就是将df的<<<索引>>>按字典分组，索引对应字典的key，最后统计的结果按字典的value呈现
# 如果原始的DataFrame中的分组信息很难确定或不存在，可以通过字典结构，定义分组信息。
wdict = {
    0: 'one',
    1: 'one',  # 索引0,1 按one分类
    2: 'two',
    3: 'two',  # 索引2,3按two分类
    4: 'three'  # 索引3 按three分类
}
ret_groupby = df.groupby(wdict)  # DataFrameGroupBy
ret_df_size = ret_groupby.size()  # Series
ret_df_sum = ret_groupby.sum()  # DataFrame
print("ret_groupby.size():\n", ret_df_size)  #
print("\nret_groupby.sum():\n", ret_df_sum)  # 将分组后df中one,two,three组中的列的值相加

print("\n------------2.4 DataFrame.groupby()按函数分组-----------------")


# 函数作为分组键的原理类似于字典，通过映射关系进行分组，但是函数更加灵活。
def judge(x):
    if x < 4:
        return 'a'
    else:
        return 'b'


ret_series = df['data1'].map(judge)  # ret是Series
print("ret_series:\n%s" % ret_series.__str__())

ret = df['data1'].groupby(ret_series)  # 返回SeriesGroupBy；
print("\nret.size():")
print(ret.size())

print("\nret.count():")
print(ret.count())

print("\nret.sum():")
print(ret.sum())

print("\nret.mean():")
print(ret.mean())
