"""
sns.kdeplot()
    绘制密度图
rugplot用于绘制毛毯图。

"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

plt.figure(figsize=(10, 5))
fig, axes = plt.subplots(1, 2)

# df_iris = pd.read_csv('iris.csv')
# df_iris=pd.DataFrame(np.arange(1,150)**2,columns=['Petal.Length'])
# df_iris=pd.DataFrame(np.ones(150),columns=['Petal.Length'])
df_iris = pd.DataFrame(np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), columns=['Petal.Length'])

# kde密度曲线；第一个figure的第1张图
sns.kdeplot(df_iris['Petal.Length'], ax=axes[0], shade=True, color='r')  # shade阴影
# 直方图；第一个figure的第1张图
sns.histplot(df_iris['Petal.Length'], ax=axes[0], color='#000000')  # 直方图

# deprecated;使用sns.displot()代替; 绘制直方图和密度图
# 第一个figure的第2张图
sns.distplot(df_iris['Petal.Length'], ax=axes[1], kde=True, rug=True, color='#ff00ff')

# sns.displot()是figure级别，会新起一个figure
sns.displot(df_iris['Petal.Length'], kind='kde', rug=True)  # 密度图，会新起一个figure;不接受ax=axes[1]

plt.show()
