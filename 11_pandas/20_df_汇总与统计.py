"""
Pandas中常用的描述性统计量:
    min():	最小值
    max():	最大值
    mean():	均值
    ptp():	极差
    median():	中位数
    std():	标准差
    var():	方差
    cov():	协方差
    sem():	标准误差
    mode():	众数
    skew():	样本偏度
    kurt():	样本峰度
    quantile():	四分位数
    count():	非空值数目
    describe():	描述统计,对每个数值型的[列]数据进行统计
    mad():	平均绝对离差

df.sum():
    对每行或者每列进行相加



"""
import pandas as pd

data = {'fruit': ['apple', 'grape', 'banana'], 'price': [70, 40, 50], 'weight': [1, 2, 3]}
df = pd.DataFrame(data)
print(df)

print("\n----------------1.df.sum()-----------------")
ret = df.sum()  # 返回Series
print('按列汇总:\n%s' % ret.__str__())

ret = df.sum(axis=1)
print('按行汇总:\n%s' % ret.__str__())

print("\n----------------2.df.describe()-----------------")
ret = df.describe()  # 返回DataFrame
print(ret)
