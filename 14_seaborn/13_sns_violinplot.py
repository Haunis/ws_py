"""
小提琴图其实是箱线图与核密度图的结合，箱线图展示了分位数的位置，
小提琴图则展示了任意位置的密度，通过小提琴图可以知道哪些位置的密度较高。
在图中，白点是中位数，黑色盒型的范围是下四分位点到上四分位点，细黑线表示须。
外部形状即为核密度估计（在概率论中用来估计未知的密度函数，属于非参数检验方法之一）。

"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

# df_iris = pd.read_csv('./iris.csv')
df_iris = pd.DataFrame()
# df_iris['Sepal.Length'] = np.arange(1, 10)
# df_iris['Petal.Length'] = np.arange(11, 20)
df_iris['Sepal.Length'] = np.random.randn(20)
df_iris['Petal.Length'] = np.random.randn(20)


ax = sns.violinplot(x=df_iris['Petal.Length'])
plt.show()
