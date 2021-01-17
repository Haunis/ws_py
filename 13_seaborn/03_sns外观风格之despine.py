"""
轴线设置相关:删除轴线，相对于轴线偏移

sns.despine(offset=20,left=True,bottom=True,trim=None)
    <<<在plt.plot()之后调用>>>
    offset:相对x轴，y轴的偏移
    left,bottom: 为True的话，去除相关轴线
    trim:当刻度没有完全覆盖整个坐标轴的的范围时,使用trim限制已有坐标轴的范围。
         就是将轴线和原点对齐


"""

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def sin_plot(flip=2):
    x = np.arange(0, 20, 0.2)
    for i in range(0, 2):
        # plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)
        plt.plot(x, np.sin(x) + i, label="y = sin(x)+%d" % i)
    plt.legend(loc="upper center")
    # plt.show()


if __name__ == "__main__":
    plt.figure(figsize=(10, 5))
    print("------------1.trim=True--------------")
    sns.set(style='whitegrid', palette='colorblind', color_codes=True)  # 在plt.plot()之前调用
    plt.subplot(1, 2, 1)
    plt.title("1. sns.despine(trim=True)")
    sin_plot()
    # sns.despine()  # 去除顶部和右侧轴线
    # sns.despine(left=True)  # 去除左侧轴线
    # sns.despine(left=True,bottom=True)  # 去除左侧和下方轴线
    sns.despine(offset=20, trim=True)  # 对轴线进行偏置; 在plt.plot()之后调用

    print("------------2.trim=False--------------")
    sns.set(style='whitegrid', palette='colorblind', color_codes=True)  # 在plt.plot()之前调用
    plt.subplot(1, 2, 2)
    plt.title("2. sns.despine(trim=False)")
    sin_plot()
    sns.despine(offset=20, trim=False)  # 对轴线进行偏置; 在plt.plot()之后调用

    plt.show()
