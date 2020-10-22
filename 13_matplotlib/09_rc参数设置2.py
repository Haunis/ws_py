"""
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
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(30).cumsum(), color='r',
        linestyle='dashed', marker='o', label='one')  # 图上的点用圆圈
ax.plot(np.random.randn(30).cumsum(), color='g',
        linestyle='dashed', marker='+', label='two')  # 点用+
ax.plot(np.random.randn(30).cumsum(), color='b',
        linestyle='dashed', marker='v', label='three')  # 点用朝下三角形
ax.legend(loc='best')  # 图列
plt.show()
