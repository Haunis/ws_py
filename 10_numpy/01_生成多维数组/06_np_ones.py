"""
生成全1多维数组

np. ones(shape, dtype=None, order='C')
    返回numpy.ndarray
    dtype:默认float64
"""

import numpy as np

print("------------1.生成全0一维数组------------------")
narray = np.ones(4)  # numpy.ndarray
print(narray)  # [1. 1. 1. 1.]

print("\n-----------2.生成多维数组------------------")
narray = np.ones([3, 4], dtype="int64")  # 3*4全1矩阵
print(narray)
print("type(ret):", type(narray))
