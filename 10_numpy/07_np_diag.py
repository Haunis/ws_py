"""
生成对角矩阵
np.diag(v, k=0)
    返回numpy.ndarray
    v:接收列表,以列表元素为矩阵对角线上元素
    k:偏移
"""
import numpy as np

ret = np.diag([1, 2, 3, 4, 5], k=0)
print(ret)
print("type(ret):", type(ret))  # numpy.ndarray