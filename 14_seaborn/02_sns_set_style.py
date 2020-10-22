"""
sns.set_style( )设置主题
    有五个预设的主题： darkgrid， whitegrid，dark，white，和 ticks，默认为darkgrid。

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


# sns.set_style('whitegrid')
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

sin_plot()
