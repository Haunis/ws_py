"""
sns.barplot(x,y,data)
    默认情况下，绘制的y轴是平均值。

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.grid()
df_iris = pd.read_csv('./iris.csv')
sns.barplot(x=df_iris['Species'], y=df_iris['Petal.Length'], data=df_iris)

df_mean = df_iris.groupby('Species').mean()
print(df_mean)

plt.subplot(1, 2, 2)
plt.grid()
df = pd.DataFrame(np.ones([9, 4]), columns=['a', 'b', 'c', 'd'])
df[:3] = df[0:3] * 1
df[3:6] = df[3:6] * 2
df[6:] = df[6:] * 3
df['a'][0] = 4
df['e'] = ['aa', 'aa', 'aa', 'bb', 'bb', 'bb', 'cc', 'cc', 'cc']
sns.barplot(x=df['e'], y=df['a'], data=df)

print(df)
plt.show()
