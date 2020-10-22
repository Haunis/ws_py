"""
isnull()函数可以直接判断某列中的哪个数据为NaN，
利用isnull().sum()可以统计缺失值的缺失数目。
"""

import numpy as np
import pandas as pd

print("------------1.df.isnull()------------\n\n")
se = pd.Series(['aa', 'bb', np.nan, 'cc'])
print(se)
ret_se = se.isnull()
print(ret_se)

print("\n------------2.df.isnull().sum()------------\n\n")
df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
df.iloc[2, :] = np.nan
df[3] = np.nan
print(df)
ret_se = df.isnull().sum()  # 统计每列为null的数量
print(ret_se)

print("\n------------3.df.info()------------\n\n")
# 查看有多少非空数值
df.info()  # 无返回值
