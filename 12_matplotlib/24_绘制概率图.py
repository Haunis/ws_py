"""
概率图模型是图灵奖获得者Pearl提出的用来表示变量间概率依赖关系的理论

正态分布又名高斯分布

正态概率密度函数:normpdf（X，mu，sigma）
    x为向量
    mu为均值
    sigma为标准差
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

fig, ax = plt.subplots()
plt.rcParams['font.family'] = ['SimHei']  # 用来显示中文

np.random.seed(1587554)
mu = 100
sigma = 15
x = mu + sigma * np.random.randn(437)
num_bins = 50
n, bins, patches = ax.hist(x, num_bins, density=1)  # 绘制直方图
y = norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')  # 绘制折线
fig.tight_layout()
plt.show()
