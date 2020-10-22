"""
概率图模型是图灵奖获得者Pearl提出的用来表示变量间概率依赖关系的理论

正态分布又名高斯分布

norm.pdf（X，mu，sigma）:正态概率密度函数
    x:向量
    mu:均值
    sigma:标准差

AxesSubplot.hist(x, bins):绘制直方图
    x:ndarray 需要的向量
    bins:分几组

"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

fig, ax = plt.subplots()
print(type(ax))
plt.rcParams['font.family'] = ['SimHei']  # 用来显示中文

np.random.seed(1587554)
mu = 100  # 均值
sigma = 15  # 标准差
x = mu + sigma * np.random.randn(437)
# x = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

num_bins = 50
n, bins, patches = ax.hist(x, bins=num_bins, density=1)  # 绘制直方图;返回一个元组,元组里有3个元素
y = norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')  # 绘制折线
fig.tight_layout()
plt.show()
