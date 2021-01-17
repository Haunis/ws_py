"""
设置缩放参数

sns.set_context(context,font_scale)
    <<<在plt.subplot()之前调用>>>
    context:预设的参数有paper, notebook, talk, poster。默认为notebook。
    font_scale: 文字缩放比例，默认1

"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def sin_plot(flip=2):
    x = np.arange(0, 20, 0.2)
    for i in range(0, 2):
        # plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)
        plt.plot(x, np.sin(x) + i)
    # plt.show()


if __name__ == "__main__":
    plt.figure(figsize=(10, 5))

    sns.set_context("talk", font_scale=3, rc={"lines.linewidth": 1.5})  # 在plt.subplot()之前调用
    plt.subplot(1, 2, 1)
    sin_plot()

    sns.set_context("notebook", font_scale=3, rc={"lines.linewidth": 1.5})
    plt.subplot(1, 2, 2)
    sin_plot()
    plt.show()
