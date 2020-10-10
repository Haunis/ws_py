"""
 np.argsort
    根据一个或多个键值对数据集进行排序
    返回的是数组值从小到大的索引值;
"""
import numpy as np

arr = np.array([7, 9, 5, 2, 9, 4, 3, 1, 4, 3])
print('原数组：', arr)
ret = arr.argsort()  # 返回索引存在narray
print('排序后：', ret)
