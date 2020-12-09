"""
np.tile(A, reps)
    一维数组直接重复几次,多维数组则横向重复
    A: 要重复的narray
    reps: 表示重复次数

另外还有narray.repeat(A, reps, axis = None)可进行重复扩张操作
"""

import numpy as np

narray = np.arange(5)
print('原数组：', narray)
narray2 = np.tile(narray, 3)
print('重复后：', narray2)

narray = np.array([[1, 2, 3], [4, 5, 6]])
print('\n原数组：\n', narray)
narray2 = np.tile(narray, 3)
print('\n重复后：\n', narray2)
