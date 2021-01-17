"""
除了选用预设的风格外，可以利用with 语句使用axes_style()方法设置临时绘图参数。

"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def sin_plot(flip=2):
    x = np.arange(0, 20, 0.2)
    for i in range(0, 2):
        # plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)
        plt.plot(x, np.sin(x) + i)
    # plt.show()


if __name__ == "__main__":
    plt.rcParams['font.family'] = ['SimHei']  # 配置中文显示
    plt.rcParams['axes.unicode_minus'] = False

    with sns.axes_style("darkgrid"):  # 临时设置成黑色格子主题
        plt.subplot(2, 1, 1)
        plt.title("1.with")
        sin_plot()

    plt.subplot(2, 1, 2)
    plt.title("2.正常绘制")
    sin_plot(-1)  # 后面的还是默认的主题

    plt.show()
