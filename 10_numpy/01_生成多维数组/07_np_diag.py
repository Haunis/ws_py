"""
生成对角矩阵
np.diag(v, k=0)
    返回numpy.ndarray
    v:接收列表,以列表元素为矩阵对角线上元素
    k:偏移
"""
import numpy as np

narray = np.diag([1, 2, 3, 4, 5], k=0)  # numpy.ndarray
print(narray)
"""
[[1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]
 [0 0 0 0 5]]
"""
