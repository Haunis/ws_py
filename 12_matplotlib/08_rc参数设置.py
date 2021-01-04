"""
pyplot使用rc配置文件来自定义图形的各种默认属性，被称为rc配置或rc参数

在pyplot中几乎所有的默认属性都是可以控制的，
例如视图窗口大小以及每英寸点数、线条宽度、颜色和样式、坐标轴、坐标和网格属性、文本、字体等。

两种方式可以设置参数:1.全局参数定制 2.rc设置方法。

###############全局参数定制 ################
全局参数定制:
    找到当前用户的配置文件目录，修改matplotlibrc文件，即可修改配置参数。
    显示当前用户的配置文件目录:print(plt_lib.matplotlib_fname())

    
全局参数配置:

配置中文参考:https://blog.csdn.net/neutionwei/article/details/108311811
1.Matplotlib存放ttf文件的路径
    import matplotlib
    print(matplotlib.matplotlib_fname())
    ~/.local/lib/python3.5/site-packages/matplotlib/mpl-data/matplotlibrc
2.将下载的字体文件复制到Matplotlib放ttf文件的路径
    ~/.local/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf
3.删除缓存
    rm ~/.cache/matplotlib/fontlist-v300.json


###############rc设置方法################
plt.plot(*args,color='r',linestyle='dashed', marker='o', label='one')
    lines.linewidth:线条宽度	取0-10之间的数值，默认为1.5。
    lines.linestyle:线条样式	可取“-”“--”“-.”“：”四种。默认为“-”。
                - : 实线
                -- : 长虚线
                -. : 点线
                : : 短虚线
    lines.marker:线条上点的形状	可取“o” “D” “h”  “.” “,” “S”等20种，默认为None。
            ‘o’	圆圈
            ‘.’	点
            ‘D’	菱形
            ‘s’	正方形
            ‘h’	六边形1
            ‘*’	星号
            ‘H’	六边形2
            ‘d’	小菱形
            ‘-’	水平线
            ‘v’	一角朝下的三角形
            ‘8’	八边形
            ‘<’	一角朝左的三角形
            ‘p’	五边形
            ‘>’	一角朝右的三角形
            ‘，’	像素
            ‘^’	一角朝上的三角形
            ‘+’	加号
            ‘\’	竖线
            ‘None’	无
            ‘x’	X
    lines.markersize:点的大小	取0-10之间的数值，默认为1
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as plt_lib


def test_fun(t):
    return np.cos(2 * np.pi * t)


def main():
    print("--------------1.第1个figure,全局参数设置------------------------")
    print("rc文件路径: ", plt_lib.matplotlib_fname())  # 查看rc文件路径
    # print(plt_lib.rc_params())  # 查看rc参数
    fig, axes = plt.subplots()
    # 配置中文显示
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x1 = np.arange(0.0, 4.0, 0.5)
    x2 = np.arange(0.0, 4.0, 0.01)
    plt.figure(1)
    plt.subplot(1, 2, 1)  # 第1个子图
    plt.plot(x1, test_fun(x1), 'bo ', x2, test_fun(x2), 'k')
    plt.title('子图1')

    plt.subplot(1, 2, 2)  # 第2个子图
    plt.plot(np.cos(2 * np.pi * x2), 'r--')
    plt.title('sub_2')
    plt.show()

    print("--------------2.第2个figure,rc设置方法------------------------")
    fig = plt.figure()
    # ax = fig.add_subplot(2, 2, 3)
    ax = plt.subplot()
    # ax.plot()可以用plt.plot（）代替
    ax.plot(np.random.randn(30).cumsum(), color='r',
            linestyle='dashed', marker='o', label='one')  # 图上的点用圆圈
    ax.plot(np.random.randn(30).cumsum(), color='g',
            linestyle='dashed', marker='+', label='two')  # 点用+
    ax.plot(np.random.randn(30).cumsum(), color='b',
            linestyle='dashed', marker='v', label='three')  # 点用朝下三角形
    ax.legend(loc='best')  # 图列

    plt.show()


if __name__ == "__main__":
    main()
