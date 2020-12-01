"""
生成单元矩阵,和matlab eye()函数一样

np.eye(num) #返回numpy.ndarray
"""
import numpy as np

narray = np.eye(4)  # numpy.ndarray
print(narray)
"""
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
"""
