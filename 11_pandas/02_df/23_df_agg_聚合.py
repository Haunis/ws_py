"""
pd.read_excel()需要xlrd支持:
    pip3 install xlrd

agg(),aggregate():
    都支持对每个分组应用某个函数,包括Python内置函数或自定义函数。
    同时，这两个方法也能够直接对DataFrame进行函数应用操作。
    在正常使用过程中，agg和aggregate函数对DataFrame对象操作的功能基本相同，因此只需掌握一个即可。

SeriesGroupBy.transform():
    将计算结果显示在每一行

SeriesGroupBy.apply()
    类似于agg方法，能够将函数应用于每一列
"""
import pandas as pd
import numpy as np

data = pd.read_excel('testdata.xls')  # 返回DataFrame

print(data.head())  # DataFrame
data.info()

print("\n---------------1.df.agg([np.sum, np.mean])--------------")
df2 = data[['淋巴细胞计数', '白细胞计数']]
# print(df2)
ret_df = df2.agg([np.sum, np.mean])  # 对每列使用np.sum,np.mean函数,且生成的DataFrame index是sum,mean
print(ret_df)

print("\n---------------2.1 df.agg(dict) --------------")
# 分别求字段的不同统计量.返回Series,且Series的index是'淋巴细胞计数','血小板计数'
ret_se = data.agg({'淋巴细胞计数': np.mean, '血小板计数': np.std})
print(ret_se)

print("\n---------------2.2 df.agg(dict)--------------")
ret_df = data.agg({'淋巴细胞计数': np.mean, '血小板计数': [np.mean, np.std]})
print(ret_df)

print("\n---------------3.SeriesGroupBy.agg(np.mean)--------------")
# 按性别分类,只取'血小板计数'这列进行统计
ret_df_groupby = data.groupby('性别')  # DataFrameGroupBy; 按性别分组
ret_se_groupby = ret_df_groupby['血小板计数']  # 取'血小板计数'这一列,返回SeriesGroupBy
ret_se = ret_se_groupby.agg(np.mean)  # 相当于ret_se_groupby.mean()
print(ret_se)

print("\n---------------4.DataFrameGroupBy.agg(np.mean)--------------")
# as_index=False返回DataFrameGroupBy，无as_index则返回SeriesGroupBy； 该参数的含义是'性别'不作为Index
ret_df_groupby = data.groupby(['性别', '是否吸烟'], as_index=False)
ret_df_groupby = ret_df_groupby['血小板计数']  # DataFrameGroupBy; 只取 ‘血小板计数’这一列
print(type(ret_df_groupby))
ret_df = ret_df_groupby.agg(np.mean)  # DataFrame
print(ret_df)

print("\n---------------5.SeriesGroupBy.transform('mean')--------------")
# transform()就是将计算结果显示在每一行
se_groupby = data.groupby(['性别', '是否吸烟'])['血小板计数']  # 返回SeriesGroupBy
se = se_groupby.transform('mean').sample(5)  # Series; 随即取5个显示
print(se)

print("\n---------------6.SeriesGroupBy.apply(np.mean)--------------")
# apply方法类似于agg方法，能够将函数应用于每一列
se_groupby = data.groupby(['性别', '是否吸烟'])['血小板计数']
se = se_groupby.apply(np.mean)
# print(se.index)
print(se)  # Index是MultiIndex
