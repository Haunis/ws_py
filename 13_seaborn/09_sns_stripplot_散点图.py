"""
stripplot绘制各变量在每个类别的值。
例：在iris数据集中，显示Petal.Width在Species上值的分布
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')
sns.set(style='white', color_codes=True)  # 设置样式
# sns.stripplot(x=df_iris['Species'], y=df_iris['Petal.Width'], data=df_iris)
# 由于散点图中数据众多，很多点会被覆盖，这时可以加入抖动（jitter=True）
sns.stripplot(x=df_iris['Species'], y=df_iris['Petal.Width'], data=df_iris, jitter=True)
sns.despine()  # 去坐标轴
plt.show()
