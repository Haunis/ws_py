"""
sns.regplot():绘制回归图,揭示两个变量间的线性关系
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('./iris.csv')
sns.regplot(x='Petal.Length', y='Petal.Width', data=df_iris)
plt.show()
