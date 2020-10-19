"""
若数据服从正态分布，在3σ原则下，异常值被定义为一组测定值中与平均值的偏差超过3倍标准差的值，
因为在正态分布的假设下，距离平均值3σ之外的值出现的概率小于0.003。
因此根据小概率事件，可以认为超出3σ之外的值为异常数据。

"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20), columns=['W'])
df['Y'] = df['W'] * 1.5 + 2  # 增加一列
df.iloc[3, 1] = 128  # 第3行,第1列元素
df.iloc[18, 1] = 150


def outRange(S):
    # 平均值的偏差超过3倍标准差的
    blidx = (S.mean() - 3 * S.std() > S) | (S.mean() + 3 * S.std() < S)  # 存储bool的Series
    # blidx = S.mean()>3*S
    idx = np.arange(S.shape[0])[blidx]  # series.shape是个元组
    # print(idx, end="\n\n")
    # print(type(idx))
    outRange = S.iloc[idx]
    return outRange


outier = outRange(df['Y'])  # 返回Series
print(outier)
