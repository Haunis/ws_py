Matplotlib 是一个在 python 下实现的类 matlab 的纯 python 的第三方库,旨在用 python实现 matlab 的功能,
是python下最出色的绘图库。其风格跟 matlab 相似，同时也继承了 python 的简单明了。
要使用matplotlib得先安装 numpy 库 (一个python下数组处理的第三方库，可以很方便的处理矩阵，数组) 。

Pyplot提供了一套和Matlab类似的绘图API，使得Matplotlib的机制更像Matlab
在Jupyter notebook中进行交互式绘图，需要执行一下语句： % matplotlib notebook或者  %matplotlib inline

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

