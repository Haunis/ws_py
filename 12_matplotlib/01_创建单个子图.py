"""
1.创建画布:fig =  plt.figure()
2.添加子图:fig.add_subplot(2,2,1) #在2*2的子图中,添加到第一个位置
"""
import matplotlib.pyplot as plt
import matplotlib as plt_lib

print(plt_lib.matplotlib_fname())  # 查看配置文件目录

fig = plt.figure()  # 创建一个空白画布，可以指定画布大小，像素。
# 不能使用空白的figure绘图，需要创建子图
ax1 = fig.add_subplot(2, 2, 1)  # 创建并选中子图，可以指定子图的行数，列数，与选中图片编号。
ax2 = fig.add_subplot(2, 2, 2)  # 返回AxesSubplot
ax3 = fig.add_subplot(2, 2, 3)
plt.show()
