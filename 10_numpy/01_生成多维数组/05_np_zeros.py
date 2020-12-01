"""
生成全0多维数组

np.zeros(shape, dtype=float, order='C')
    返回numpy.ndarray
"""

import numpy as np

print("-------------1.生成一维全0数组------------------")
narray = np.zeros(4)  # 返回 <class 'numpy.ndarray'>
print(narray)  # [0. 0. 0. 0.]
print("narray.dtype:", narray.dtype) # 默认float64

print("\n------------2.生成多为数组------------------")
narray = np.zeros([3, 4])  # 返回numpy.ndarray; 3*4全0矩阵
print(narray)

