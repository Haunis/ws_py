"""
np.tile(A, reps)
    一维数组直接重复几次,多维数组则横向重复
    A: 要重复的narray
    reps: 表示重复次数

另外还有narray.repeat(A, reps, axis = None)可进行重复操作
"""

import numpy as np

arr = np.arange(5)
# arr = np.random.randint(0, 10, (4, 4)) #多维数组横向重复
print('原数组：', arr)
wy = np.tile(arr, 3)
print('重复数据处理：\n', wy)
