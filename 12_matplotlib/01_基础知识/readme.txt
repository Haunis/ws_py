Matplotlib简介：
    Matplotlib是一个在python下实现的类matlab的纯python的第三方库,旨在用python实现 matlab 的功能
    其风格跟matlab相似，同时也继承了python的简单明了。
    要使用matplotlib得先安装numpy库 (一个python下数组处理的第三方库，可以很方便的处理矩阵，数组) 。

Pyplot提供了一套和Matlab类似的绘图API，使得Matplotlib的机制更像Matlab
在Jupyter notebook中进行交互式绘图，需要执行一下语句： % matplotlib notebook或者  %matplotlib inline

-------------------------------------------------
1.创建画布:
    非必须,不创建的话默认使用同一个
    plt.figure(num)   num: 不指定的话就自动增长，从1～N 相当于画布的id
    fig, axes = plt.subplots(2, 3) 创建新的画布，并返回新的子图

2.在画布上添加子图:
    ax = fig.add_subplot(2, 2, 1) #注意subplot()从1开始
    ax = plt.subplot(2,2,1)
    fig, axes = plt.subplots(2, 3) #注意axes[index]从0开始

3.绘制曲线:
    plt.subplot(2,2,1)
    ax.plot(pd.Series(np.arange(0, 2)))

    axes[1][2].plot([1, 2, 3, 4])
    axes[1,2].plot([1, 2, 3, 4])

-------------------------------------------------
matplotlib相关函数:
   figure（）：创建一个新的绘图窗口。
   figtext（）：为figure添加文字
   axes（）：为当前figure添加一个坐标轴
   plot（）：绘图函数
   polar（）：绘制极坐标图
   axis（）：获取或设置轴属性的边界方法（坐标的取值范围）
   clf   ： 清除当前figure窗口          cla  ： 清除当前axes窗口
   close      ： 关闭当前figure窗口
   subplot    ： 一个图中包含多个axes
   text（）： 在轴上添加文字
   title（）： 设置当前axes标题
   xlabel/ylabel：设置当前X轴或Y轴的标签
   hist（）：绘制直方图
   hist2d（）：绘制二维在直方图
   hold      ：设置当前图窗状态；off或者on
   imread（）：读取一个图像，从图形文件中提取数组
   legend（）：为当前axes放置标签
   pie（）：绘制饼状图
   scatter（）：做一个X和Y的散点图，其中X和Y是相同长度的序列对象
   stackplot（）：绘制一个堆叠面积图
   acorr（）：绘制X的自相关函数
   annotate（）：用箭头在指定的数据点创建一个注释或一段文本
   bar（）：绘制垂直条形图		 barh（）：绘制横向条形图
   barbs（）：绘制一个倒钩的二维场


