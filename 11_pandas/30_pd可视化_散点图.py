"""
通过plot函数的kind = 'scatter'可以进行绘制。

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.DataFrame(np.arange(0, 10, 0.1), columns=['A'])
print(df)
df['B'] = 2 * df['A'] + 4
df['C'] = df['A'].map(math.sin)
print("-------------")
print(df)
df.plot(kind='scatter', x='A', y='B')
df.plot(kind='scatter', x='A', y='C')

plt.show()
