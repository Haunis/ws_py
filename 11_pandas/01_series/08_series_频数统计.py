"""
对于类别型特征的描述性统计，可以使用频数统计表。
Series.unique(): 返回不重复的数组(ndarray)
Series.value_counts: 返回每个value的个数(返回的还是Series)

"""
import pandas as pd

se = pd.Series(['a', 'b', 'c', 'd', 'a', 'c'])
print("原se:\n%s" % se.__str__())

print("\n--------------1.series.unique()-------------")
ret_ndarray = se.unique()  # 去重,返回ndarray
print(ret_ndarray)

print("\n--------------2.series.value_counts()-------------")
ret_series = se.value_counts()  # 统计Series每个values的个数，返回Series
print(ret_series)
