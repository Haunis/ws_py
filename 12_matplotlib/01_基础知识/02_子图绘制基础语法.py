"""

plt常用语法：
    plt.title()	    在当前图形中添加标题，可以指定标题的名称、位置、颜色、字体大小等参数。
    plt.tick_params()   显示的xticks,yticks字体大小
    plt.xlabel()	在当前图形中添加x轴名称，可以指定位置、颜色、字体大小等参数。
    plt.ylabel()    在当前图形中添加y轴名称，可以指定位置、颜色、字体大小等参数。
    plt.xlim()	    指定当前图形x轴的范围，只能确定一个数值区间，而无法使用字符串标识。
    plt.ylim()	    指定当前图形y轴的范围，只能确定一个数值区间，而无法使用字符串标识。
    plt.xticks()	指定x轴刻度的数目与取值。
    plt.yticks()	指定y轴刻度的数目与取值。
    plt.legend()	指定当前图形的图例，可以指定图例的大小、位置、标签。

语法运用之sticks():
    设置x轴刻度和标签标签:
    方式1:
        ax.set_xticks(ticks = [0, 5, 10, 15, 20, 25, 30, 40])
        ax.set_xticklabels(labels = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh'])
    方式2：
        plt.xticks(ticks=ticks, labels=labels)

语法运用之legend():
    plt.legend(loc,,,)
    loc属性：
        ’best’          ‘center’          ‘right’
        ‘upper left’    ‘upper center’   ‘upper right’
        ‘lower left’    ‘lower center’   ‘lower right’
        ‘center left’   ‘center center’  ‘upper right’
    常用如下:
        plt.legend(loc = 'best',frameon = False) #去掉图例边框,推荐使用
        plt.legend(loc = 'best',edgecolor = 'blue') #设置图例边框颜色
        plt.legend(loc = 'best',facecolor = 'blue')#设置图例背景颜色,若无边框,参数无效

"""
import numpy as np
import matplotlib.pyplot as plt

data = np.arange(0, np.pi * 2, 0.1)
fig = plt.figure(figsize=(8, 4), dpi=90)  # 确定画布大小

print("------------1.plt.plot()-------------------")
ax = plt.subplot(1, 2, 1)  # 绘制第1幅子图; 返回ax，但不使用
plt.title('1st : sin/cos')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, np.pi * 2)
plt.ylim(-1, 1)
plt.xticks([0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2])  # x轴刻度的数目与取值。
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.tick_params(labelsize=16)  # 显示的xticks,yticks字体大小
plt.plot(data, np.sin(data))
plt.plot(data, np.cos(data))
plt.legend(['sin', 'cos'], loc='upper center')

print("------------2.ax.plot()-------------------")
ax = fig.add_subplot(1, 2, 2)  # 绘制第2幅子图
plt.title('2st : lines example')
plt.xlabel('X-cori')
plt.ylabel('Y-cori')
plt.xlim(0, 1)  # 范围
plt.ylim(0, 1)  # 范围

# plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # ok
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # y轴显示的数值
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # 要加入这行,否则ax.set_xticklabels()会有warning提示
ax.set_xticklabels(labels=['a', 'b', 'c', 'd', 'e', 'f'], rotation=30, fontsize='large')

ax.plot(data, data)
ax.plot(data, data ** 2)
ax.plot(data, data ** 3)
plt.legend(['y=x', 'y = x^2', 'y = x^3'], loc='best')

plt.show()
