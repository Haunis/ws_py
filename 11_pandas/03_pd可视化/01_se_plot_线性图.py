"""
Series和DataFrame都有一个plot属性，用于绘制基本的图形
默认情况下，plot（）绘制的都是折线
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# % matplotlib inline #jupyter notebook使用在代码下方直接显示图片

print('------------1.Series.plot()---------')
nda = np.arange(0, 10, 0.1)
se = pd.Series(np.sin(nda), index=nda)
se.plot(marker='o')  # 绘制第一张图

print('------------2.df.plot()---------')
df = pd.DataFrame({'normal': np.random.normal(size=50),
                   'gamma': np.random.gamma(1, size=50)})  # 伽马分布常被用来模拟电子元件的失效时间
# print(df)
df.plot(marker='o')  # 绘制第二张图
plt.show()  # pycharm要使用这行代码才能显示图片
