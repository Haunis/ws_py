"""
利用distplot函数可以同时绘制直方图、密度图和毛毯图.

同时，这些分布图都有对应的专门函数其中，kdeplot函数绘制密度图，rugplot用于绘制毛毯图。

"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# df_iris = pd.read_csv('iris.csv')
# df_iris=pd.DataFrame(np.arange(1,150)**2,columns=['Petal.Length'])
# df_iris=pd.DataFrame(np.ones(150),columns=['Petal.Length'])
df_iris = pd.DataFrame(np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), columns=['Petal.Length'])

fig, axes = plt.subplots(1, 2)
sns.set_style('darkgrid')
sns.distplot(df_iris['Petal.Length'], ax=axes[0], kde=True, rug=True)  # 第一个图绘制直方图和密度图

# kde密度曲线，rug边际毛毯
sns.kdeplot(df_iris['Petal.Length'], ax=axes[1], shade=True)  # shade阴影

plt.show()
