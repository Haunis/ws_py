"""
Matplotlib绘图基本模仿MATLAB绘图库，其绘图风格和MATLAB类似,绘图风格偏古典
Seaborn是对对Matplotlib进行封装，绘图效果更符合现代人的审美
Seaborn属于Matplotlib的一个高级接口，使得作图更加容易。在多数情况下使用Seaborn能做出很具吸引力的图
而使用Matplotlib可以制作具有更多特色的图
应该把Seaborn视为Matplotlib的补充，而不是替代物

风格设置:
    以设置绘图的背景色、风格、字型、字体等

Seaborn通过set函数实现风格设置:
    seaborn.set(context='notebook', style='darkgrid', palette='deep',
                font='sans-serif', font_scale=1, color_codes=True, rc=None)
        在plt.subplot()之前调用
        style: 5个预设主题 darkgrid,whitegrid,dark,white,ticks. 默认为darkgrid。
                也可以使用sns.set_style()进行设置
        palette: 调色板； 有deep, muted, bright, pastel, dark, colorblind，默认deep

Seaborn将matplotlib的参数划分为两个独立的组合:
    第一组: 设置绘图的外观风格的
        axes_style():会返回一组字典参数
        set_style():设置matplotlib默认参数; 在plt.subplot()之前调用
    第二组: 主要将绘图的各种元素按比例缩放的，以至可以嵌入到不同的背景环境中。
        缩放绘图：
        plotting_context():会返回一组字典参数
        set_context():设置matplotlib默认参数;  在plt.subplot()之前调用



"""

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def sin_plot(flip=2):
    x = np.arange(0, 20, 0.2)
    for i in range(1, 5):
        plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)
    # plt.show()


if __name__ == "__main__":
    plt.figure(figsize=(10, 5))

    print("---------------1.sns.set()------------------")
    # sns.set()  # seaborn默认的绘图设置
    sns.set(style='darkgrid', font_scale=1.5)  # 设置黑色格子; 在plt.subplot()之前调用
    plt.subplot(1, 2, 1)
    plt.title("sns.set()")  # 在plt.subplot()之后调用
    sin_plot()

    print("---------------2.sns.set_style()------------------")
    sns.set_style("whitegrid", {"axes.facecolor": ".10"}) #在plt.subplot()之前调用
    plt.subplot(1, 2, 2)
    plt.title("sns.set_style()")
    sin_plot()

    plt.show()
