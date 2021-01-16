"""
1.创建画布:
    方式1：
        fig =  plt.figure(num,figsize=(10, 15))
            num: 不指定的话就自动增长，从1～N 相当于画布的id
            figsize:指定大小
    方式2：
        fig, axes = plt.subplots(2, 3)
            创建新画布的同时，也创建了2*3个子图
2.添加子图:
    方式1：ax = fig.add_subplot(2,2,1) #在2*2的子图中,添加到第一个位置
    方式2：ax = plt.subplot(2, 2, 2)

3.绘制
    方式1：plt.plot([1, 2, 3],color = 'r')
    方式2：ax.plot([1, 2, 3], color='r')

"""
import matplotlib.pyplot as plt
import matplotlib as plt_lib

print("matplotlib文件目录：", plt_lib.matplotlib_fname())  # 查看配置文件目录

# 创建一个空白画布，可以指定画布大小，像素。
fig = plt.figure(1)  # 返回Figure;

print('----------1.fig.add_subplot()-----------------')
# 创建并选中子图，可以指定子图的行数，列数，与选中图片编号。
ax = fig.add_subplot(2, 2, 1)  # 返回AxesSubplot;
# ax.plot([1, 2, 3], color='r')  # ok
plt.plot([1, 2, 3], color='r')

print('----------2.plt.subplot()-----------------')
ax = plt.subplot(2, 2, 2)  # 返回AxesSubplot;
# ax.plot([3, 2, 1], color='g') # ok
plt.plot([3, 2, 1], color='g')

print('----------3.plt.subplots(2, 3)-----------------')
# 创建1个figure,里面有2*3个子图
# fig, [ax1,ax2,ax3] = plt.subplots(2, 3) #可以用[ax1,ax2,ax3] 接收
fig, axes = plt.subplots(2, 3)  # axes是二维ndarray;

print("axes.shape:", axes.shape)  # (2,3)即2行3列的数组

fig.add_subplot(2, 3, 1)  # 添加第一个子图
plt.plot([1, 2, 3, 4], color='r')  # 第一个子图上绘制

axes[0, 1].plot([1, 2, 3, 4], color='g')  # 第二个图上绘制
axes[0][2].plot([1, 2, 3, 4], color='b')  # 第三个图上绘制

plt.show()
