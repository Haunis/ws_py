"""
有时散点图表达的值的分布信息有限，因此需要一些其它的绘图
箱线图可以观察四分位数、中位数和极值。Seaborn中利用boxplot( )绘制箱线图
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('iris.csv')
sns.set(style="ticks")  # 设置主题样式
sns.boxplot(x=df_iris['Species'], y=df_iris['Petal.Width'])
plt.show()
