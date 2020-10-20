"""
pyplot使用rc配置文件来自定义图形的各种默认属性，被称为rc配置或rc参数
在pyplot中几乎所有的默认属性都是可以控制的，
例如视图窗口大小以及每英寸点数、线条宽度、颜色和样式、坐标轴、坐标和网格属性、文本、字体等。

两种方式可以设置参数:1.全局参数定制 2.rc设置方法。

全局参数定制:
    1.print(plt_lib.matplotlib_fname())  #显示当前用户的配置文件目录
    2.找到当前用户的配置文件目录，修改matplotlibrc文件，即可修改配置参数。
    
本demo采取的全局参数配置,但由于无SimHei字体文件所以会配置失败
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as plt_lib


def test_fun(t):
    return np.cos(2 * np.pi * t)


def main():
    print(plt_lib.matplotlib_fname())  # 查看rc文件路径
    # print(plt_lib.rc_params())  # 查看rc参数
    fig, axes = plt.subplots()
    # 配置中文显示
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x1 = np.arange(0.0, 4.0, 0.5)
    x2 = np.arange(0.0, 4.0, 0.01)
    plt.figure(1)
    plt.subplot(2, 2, 1)
    plt.plot(x1, test_fun(x1), 'bo ', x2, test_fun(x2), 'k')
    plt.title('子图1')
    plt.subplot(2, 2, 2)
    plt.plot(np.cos(2 * np.pi * x2), 'r--')
    plt.title('sub_2')
    plt.show()


if __name__ == "__main__":
    main()
