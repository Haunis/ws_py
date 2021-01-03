"""
plt.title	在当前图形中添加标题，可以指定标题的名称、位置、颜色、字体大小等参数。
plt.xlabel	在当前图形中添加x轴名称，可以指定位置、颜色、字体大小等参数。
plt.ylabel	在当前图形中添加y轴名称，可以指定位置、颜色、字体大小等参数。
plt.xlim	指定当前图形x轴的范围，只能确定一个数值区间，而无法使用字符串标识。
plt.ylim	指定当前图形y轴的范围，只能确定一个数值区间，而无法使用字符串标识。
plt.xticks	指定x轴刻度的数目与取值。
plt.yticks	指定y轴刻度的数目与取值。
plt.legend	指定当前图形的图例，可以指定图例的大小、位置、标签。

plt.legend:
    Legend 图例就是为了帮助我们展示每个数据对应的图像名称，更好的让读者认识到数据结构
        0: ’best’
        1: ‘upper right’
        2: ‘upper left’
        3: ‘lower left’
        4: ‘lower right’
        5: ‘right’
        6: ‘center left’
        7: ‘center right’
        8: ‘lower center’
        9: ‘upper center’
        10: ‘center’
    常用如下:
        plt.legend(loc = 'best',frameon = False) #去掉图例边框,推荐使用
        plt.legend(loc = 'best',edgecolor = 'blue') #设置图例边框颜色
        plt.legend(loc = 'best',facecolor = 'blue')#设置图例背景颜色,若无边框,参数无效
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.arange(0, 1, 0.01)
plt.title('my lines example')
plt.xlabel('X')  # x轴标签
plt.ylabel('Y')
plt.xlim(0, 1)  # 范围
plt.ylim(0, 1)  # 范围
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1]) # x轴刻度的数目与取值。
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.tick_params(labelsize=22)  # 显示的xticks,yticks字体大小
plt.plot(data, data ** 2)  # 绘制第一个图
plt.plot(data, data ** 3)  # 绘制第二个图
plt.plot(data, data) #绘制第三个图
plt.legend(['y = x^2', 'y = x^3','y = x'],loc='lower right') #指定当前图形的图例
plt.show()
