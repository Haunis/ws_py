"""
如果需要看清每个数据点，可以使用swarmplot函数
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('iris.csv')
sns.set(style='white', color_codes=True)  # 设置样式

sns.swarmplot(x=df_iris['Species'], y=df_iris['Petal.Width'], data=df_iris)
sns.despine()  # 去坐标轴
plt.show()
