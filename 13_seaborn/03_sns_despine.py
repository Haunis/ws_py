"""
despine（）方法中可以利用offset参数讲轴线进行偏置，另外，
当刻度没有完全覆盖整个坐标轴的的范围时，利用trim参数限制已有坐标轴的范围。


"""

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def sin_plot(flip=2):
    x = np.arange(0, 20, 0.2)
    for i in range(1, 5):
        plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)
    plt.show()


sns.set(style='whitegrid',palette='muted',color_codes=True)

sin_plot()

# sns.despine()  # 去除顶部和右侧轴线,,pycharm貌似没啥用
# sns.despine(left=True)  # 去除左侧轴线,,pycharm无效
sns.despine(left=True,bottom=True)  # 去除左侧和下方轴线,,pycharm无效
# sns.despine(offset=20, trim=True)  # 对轴线进行偏置,pycharm无效
