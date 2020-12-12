"""
Series和DataFrame都有一个plot属性，用于绘制基本的图形
默认情况下，plot（）绘制的都是折线
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# % matplotlib inline #jupyter notebook使用在代码下方直接显示图片

# series.plot()
x = np.arange(0, 10, 0.1)
se = pd.Series(np.sin(x), index=x)
se.plot(marker='o')

# df.plot()
df = pd.DataFrame({'normal': np.random.normal(size=50),
                   'gamma': np.random.gamma(1, size=50)})  # 伽马分布常被用来模拟电子元件的失效时间
print(df)
df.plot(marker='o')
plt.show()  # pycharm要使用这行代码才能显示图片
