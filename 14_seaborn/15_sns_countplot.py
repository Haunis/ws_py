"""
sns.countplot():绘制类别的计数柱状图
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('./iris.csv')
sns.countplot(x='Species', data=df_iris)
plt.grid()
plt.show()

print(df_iris.groupby('Species').count())
