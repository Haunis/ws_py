"""
如果需要合并的两个DataFrame存在重复索引，
则使用merge和concat都无法正确合并，此时需要使用combine_first方法
"""
import pandas as pd

s1 = pd.Series([1, 11], index=['a', 'b'])
s2 = pd.Series([3, 33], index=['f', 'g'])
s3 = pd.concat([s1 * 5, s2], sort=True)
df1 = pd.concat([s1, s3], axis=1, sort=False)  # 将Series和DataFrame 连接
df2 = pd.concat([s1, s3], axis=1, join='inner', sort=False)
print(df1, end="\n\n")
print(df2, end="\n\n")

ret_def = df2.combine_first(df1)
# ret_def = pd.merge(df1, df2, how="left")
print(ret_def)
