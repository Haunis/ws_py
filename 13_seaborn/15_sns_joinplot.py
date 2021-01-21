"""
在matplotlib中，使用散点图的方法绘制两个变量的分布关系

在Seaborn中，使用jointplot函数绘制一个多面板图，不仅可以显示两个变量的关系，还可以显示每个单变量的分布情况。

sns.jointplot()
    改变kind参数为kde，但变量的分布就用密度图来代替，而散点图则会被等高线图代替。

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('./iris.csv')
sns.jointplot(x='Petal.Length', y='Petal.Width', data=df_iris, kind='kde')  # 指定kind

df_iris = pd.DataFrame(np.ones([9, 4]), columns=['a', 'b', 'Petal.Width', 'Petal.Length'])
df_iris[:4] = df_iris[0:4] * 1  # [0,4)行
df_iris[4:6] = df_iris[4:6] * 2  # [4,6)行
df_iris[6:] = df_iris[6:] * 3  # 第6行到最后一行
df_iris['Species'] = ['aa', 'aa', 'aa', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc']
df_iris['Petal.Width'] = df_iris['Petal.Width'] * 2
print(df_iris)
sns.jointplot(x='Petal.Length', y='Petal.Width', data=df_iris)  # 指定kind='kde'会报错

plt.show()
