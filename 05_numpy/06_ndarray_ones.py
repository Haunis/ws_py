"""
生成全1矩阵

np. ones(shape, dtype=None, order='C')
返回numpy.ndarray
    dtype:默认float64
"""

import numpy as np

print("------------2.生成行向量------------------")
ret = np.ones(4)
print(ret)
print("type(ret):", type(ret))  # numpy.ndarray
print("ret.dtype:",ret.dtype) # 默认float64

print("\n------------2.生成矩阵------------------")
ret = np.ones([3, 4],dtype="int64")  # 3*4全1矩阵
print(ret)
print("type(ret):", type(ret))
