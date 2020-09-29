"""
NumPy中提供了很多用于统计分析的函数，常见的有sum、mean、std、var、min和max等。
      几乎所有的统计函数在针对二维数组的时候需要注意轴的概念。
      axis=0时表示沿着纵轴进行计算，axis=1时沿横轴进行计算

"""
import numpy as np

arr = np.arange(20).reshape(4, 5)
print('创建的数组：\n', arr)
print('数组的和：', np.sum(arr))  # 所有数的和
print('数组纵轴的和：', np.sum(arr, axis=0))  # 返回一个narray
print('数组横轴的和：', np.sum(arr, axis=1))
print('数组的均值：', np.mean(arr))  # 所有元素的平均值
print('数组横轴的均值：', np.mean(arr, axis=1))
print('数组的标准差：', np.std(arr))
print('数组横轴的标准差：', np.std(arr, axis=1))
