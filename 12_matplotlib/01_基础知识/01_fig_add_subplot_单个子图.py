"""
1.创建画布:fig =  plt.figure(num)
    num: 不指定的话就自动增长，从1～N 相当于画布的id
2.添加子图:fig.add_subplot(2,2,1) #在2*2的子图中,添加到第一个位置
"""
import matplotlib.pyplot as plt
import matplotlib as plt_lib

print("matplotlib文件目录：", plt_lib.matplotlib_fname())  # 查看配置文件目录

# 创建一个空白画布，可以指定画布大小，像素。
fig = plt.figure(1)  # 返回Figure;

# 创建并选中子图，可以指定子图的行数，列数，与选中图片编号。
ax1 = fig.add_subplot(2, 2, 1)  # 返回AxesSubplot;
plt.plot([1, 2, 3])  # 绘制

ax2 = fig.add_subplot(2, 2, 2)
plt.plot([3, 2, 1])

# ax3 = fig.add_subplot(2, 2, 3)
plt.subplot(2, 2, 3)  # 也可以用这个
plt.plot([3, 3, 3])

# ax3 = fig.add_subplot(2, 2, 4)
plt.subplot(2, 2, 4)
plt.plot([4, 4, 4])

plt.show()
