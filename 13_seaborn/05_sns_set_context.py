"""
seaborn中通过set_context()设置缩放参数
预设的参数有paper, notebook, talk, poster。默认为notebook。

"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def sin_plot(flip=2):
    x = np.arange(0, 20, 0.2)
    for i in range(1, 5):
        plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)
    plt.show()


# sns.set_context("talk")  # 设置缩放参数
sns.set_context("notebook", font_scale=3.8, rc={"lines.linewidth": 1.5})
sin_plot()
