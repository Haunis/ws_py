"""
生成全0矩阵

np.zeros(shape, dtype=float, order='C')
返回numpy.ndarray
"""

import numpy as np

print("------------2.生成行向量------------------")
ret = np.zeros(4)
print(ret)
print("type(ret):", type(ret))  # numpy.ndarray

print("\n------------2.生成矩阵------------------")
ret = np.zeros([3, 4])  # 3*4全0矩阵
print(ret)
print("type(ret):", type(ret))
