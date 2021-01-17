"""
直方图和密度曲线图:
sns.distplot():
    --->已经过失，使用sns.displot()代替<---
    可以同时绘制直方图、密度图和毛毯图.是AxesSubplot.hist(x, bins)加强版.
    默认情况下绘制一个直方图，并嵌套一个对应的密度图。



    distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None,
             hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None,
             color=None, vertical=False, norm_hist=False, axlabel=None,
             label=None, ax=None):
            hist: True-绘制直方图, False-不绘制直方图
            kde: True-绘制密度图, False-不绘制密度图
            rug: 绘制毛毯图，可以为每个观测值绘制小细线（边际毛毯），也可以单独用rugplot进行绘制。

sns.displot(data,kind,rug):
    用来代替sns.distplot()
    kind: kde,hist等等
    rug:是否绘制毛毯图

"""
# 绘制iris数据集中Petal.Width的分布图
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_iris = pd.read_csv('iris.csv')
sns.set(color_codes=True)

print("----------1.sns.displot()--------------")
sns.histplot(df_iris['Petal.Width'], color='r')  # 直方图
plt.title("1. sns.histplot()")

print("----------2.sns.distplot()--------------")
plt.figure()  # 新起一个figure否则distplot()绘制不出来
# sns.distplot(df_iris['Petal.Width'])
# sns.distplot(df_iris['Petal.Width'], bins=30, kde=False, rug=True)  # 不绘制密度图
sns.distplot(df_iris['Petal.Width'], hist=True, rug=True, color='g')  # deprecated;绘制直方图和密度图
plt.title("2. sns.distplot()")

print("----------3.sns.displot()--------------")
# 该方法是figure级别，会新起一个figure
sns.displot(df_iris['Petal.Width'], kind='hist', rug=True, color='b')  # 密度图； 代替distplot
plt.title("3.sns.displot()")

plt.show()
