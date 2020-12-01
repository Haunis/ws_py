"""
 np.argsort
    根据一个或多个键值对数据集进行排序
    返回的是数组值从小到大的索引值;
"""
import numpy as np

arr = np.array([7, 8, 5, 2, 9, 4, 0, 1, 6, 3])
print('原数组：', arr)
arr_index = arr.argsort()  # 返回索引存在narray
print('排序后：', arr_index)  # [7 3 6 9 5 8 2 0 1 4]

arr_ret = np.zeros(arr.shape[0])  # 使用索引构建排序后的数组
for index in range(arr_index.shape[0]):
    arr_ret[index] = arr[arr_index[index]]
print(arr_ret)
