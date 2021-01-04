"""
 pairplot:
    实现数据特征的两两对比。默认是所有特征，可以通过vars参数指定部分特征。
    pairplot主要展现的是变量两两之间的关系（线性或非线性，有无较为明显的相关关系）

seaborn.pairplot(data, hue=None, hue_order=None, palette=None, 
    vars=None, x_vars=None, y_vars=None, kind='scatter',
    diag_kind='auto', markers=None, height=2.5, aspect=1, dropna=True,
    plot_kws=None, diag_kws=None, grid_kws=None, size=None)


"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# df_iris = pd.read_csv('./iris.csv')

df_iris = pd.DataFrame()
df_iris['Sepal.Length'] = np.arange(1, 10)
df_iris['Petal.Length'] = np.arange(11, 20)

sns.set(style="ticks")
g = sns.pairplot(df_iris, vars=['Sepal.Length', 'Petal.Length'])
plt.show()
