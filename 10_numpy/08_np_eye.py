"""
生成单元矩阵,和matlab eye()函数一样
np.eye(num) #返回numpy.ndarray
"""
import numpy as np

ret = np.eye(4)
print(ret)
print("type(ret):", type(ret))  # numpy.ndarray
