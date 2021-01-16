"""
概率图模型是图灵奖获得者Pearl提出的用来表示变量间概率依赖关系的理论

正态分布又名高斯分布

norm.pdf（X，mu，sigma）:正态概率密度函数
    x:向量
    mu:均值
    sigma:标准差

ax.hist(x, bins)
    绘制直方图
    x:ndarray 需要的向量
    bins:分几组

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def gen_norm_data():
    data = list()
    for i in range(1, 21, 1):
        num = i if i < 10 else 21 - i
        for j in range(1, num + 1, 1):
            data.append(i)
    return data


if __name__ == "__main__":
    print('---------------1.随机生成数据----------------------')

    fig, ax = plt.subplots()  # AxesSubplot
    plt.rcParams['font.family'] = ['SimHei']  # 用来显示中文

    np.random.seed(1587554)
    mean = 100  # 均值
    sigma = 15  # 标准差
    x = mean + sigma * np.random.randn(437)

    num_bins = 50
    n, bins, patches = ax.hist(x, bins=num_bins, density=1)  # 绘制直方图;返回一个元组,元组里有3个元素
    y = norm.pdf(bins, mean, sigma)
    ax.plot(bins, y, '--')  # 绘制折线
    fig.tight_layout()

    print('---------------2.自己生成数据----------------------')
    fig = plt.figure()  # 新起一个画布
    data = gen_norm_data()
    n, bins, patches = plt.hist(data, bins=10, density=1)  # 绘制直方图;返回一个元组,元组里有3个元素
    print("n:", n)  # 每个长方柱占的比例，纵坐标？
    print("bins:", bins)  # 每个长方柱x轴开始坐标
    print("patches:", patches)
    mean = pd.Series(data).mean()  # 均值
    sigma = pd.Series(data).std() ** 0.5  # 标准差
    y = norm.pdf(bins, mean, sigma)
    plt.plot(bins, y, '--')  # 绘制折线

    # pd.Series(data).plot(kind='hist', bins=10, grid=True)

    plt.show()
