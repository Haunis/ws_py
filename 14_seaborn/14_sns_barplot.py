"""
在Seaborn中使用barplot函数绘制柱状图，默认情况下，绘制的y轴是平均值。

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('./iris.csv')

# df_iris = pd.DataFrame(np.ones([9, 4]),columns=['a','b','c','Petal.Length'])
# df_iris[:3] = df_iris[0:3] * 0.1
# df_iris[3:6] = df_iris[3:6] * 0.2
# df_iris[6:] = df_iris[6:] * 0.3
# df_iris['Species'] = ['aa','aa','aa','bb','bb','bb','cc','cc','cc']

sns.barplot(x=df_iris['Species'], y=df_iris['Petal.Length'], data=df_iris)
plt.grid()
plt.show()

df_mean = df_iris.groupby('Species').mean()
print(df_mean)
