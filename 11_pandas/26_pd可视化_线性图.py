"""
默认是线形图
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# % matplotlib inline #jupyter notebook使用在代码下方直接显示图片
s = pd.Series(np.arange(0, 10))

s.plot()
# plt.plot(s)
plt.show()  # pycharm要使用这行代码才能显示图片

df = pd.DataFrame({'normal': np.random.normal(size=50),
                   'gamma': np.random.gamma(1, size=50)})  # 伽马分布常被用来模拟电子元件的失效时间
print(df)
df.plot()
plt.show()
