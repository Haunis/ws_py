"""
和数据库中的表分组很像

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

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['yes', 'no', 'yes', 'yes', 'no'],
                   'data1': [1, 2, 3, 4, 5],
                   'data2': [10, 20, 30, 40, 50]})
print(df, end="\n\n")

print("\n------------1.Series.groupby(series)-----------------")
grouped = df['data1'].groupby(df['key1'])  # grouped是SeriesGroupBy; df['data1']得到的是Series
print("grouped.size():")
print(grouped.size(), end="\n\n")  # grouped.size()得到的是Series

print("grouped.mean():")
print(grouped.mean(), end="\n\n")  # grouped.mean()得到的是Series

print("grouped.sum():")
print(grouped.sum(), end="\n\n")

print("\n------------2.1 DataFrame.groupby(key2)按列分组-----------------")
# DataFrame数据的列索引名可以作为分组键，但需要注意的是用于分组的对象必须是DataFrame数据本身，否则搜索不到索引名称会报错。
# df.groupby('key2')返回的是 DataFrameGroupBy
df_key2_mean = df.groupby('key2').mean()  # df_key2_mean是DataFrame
print("grouped_key2_mean:")
print(df_key2_mean.applymap(lambda x: "%.2f" % x))

print("\n------------2.2 DataFrame.groupby(key1,key2)按列分组-----------------")
print(df.groupby(['key1','key2']).mean())

print("\n------------2.3 DataFrame.groupby()按指定字典分组-----------------")
# 如果原始的DataFrame中的分组信息很难确定或不存在，可以通过字典结构，定义分组信息。
# df = pd.DataFrame(np.random.normal(size=(6, 5)), index=['a', 'b', 'c', 'A', 'B', 'c'])
df = pd.DataFrame(np.arange(1, 31).reshape(6, 5), index=['a', 'b', 'c', 'A', 'B', 'c'])
print("df:\n%s" % df.__str__())

wdict = {'a': 'one',
         'A': 'one',  # df中a index ,A index最终按one index在DataFrame显示(就是下面的ret_df)
         'b': 'two',
         'B': 'two',
         'c': 'three'}
ret_groupby = df.groupby(wdict)  # ret是DataFrameGroupBy
ret_df = ret_groupby.sum()  # ret_df是DataFrame
print("分组汇总后的结果为:\n", ret_df)  # 将df中a和A两行进行列相加(a,A在字典中对应的value都是one), b和B两行进行列相加，c行单独不相加

print("\n------------2.4 DataFrame.groupby()按函数分组-----------------")


# 函数作为分组键的原理类似于字典，通过映射关系进行分组，但是函数更加灵活。
def judge(x):
    if x >= 4:
        return 'a'
    else:
        return 'b'


df = pd.DataFrame(np.random.randint(0, 10, (4, 4)))
print(df)
print("---")
ret_series = df[3].map(judge)  # ret是Series
print("ret_series:\n%s" % ret_series.__str__())

ret = df[3].groupby(ret_series)  # 返回SeriesGroupBy；
print("\nret.sum():")
print(ret.sum())

print("\nret.count():")
print(ret.count())

print("\nret.mean():")
print(ret.mean())
