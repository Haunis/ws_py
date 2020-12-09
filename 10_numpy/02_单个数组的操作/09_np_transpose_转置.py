"""
获取多维数组的转置:
    方式1:np.transpose(narray,(1,0))
    方式2:narray.transpose((1,0)) #注意参数是元组
    方式3:narray.T #使用narray的T属性获取转置
"""

import numpy as np

narray = np.arange(6).reshape(3, 2)
print("origin data:\n", narray)
"""
 [[0 1]
 [2 3]
 [4 5]]
"""

narray2 = np.transpose(narray, (1, 0))
# narray2 = ret.transpose((1, 0))
# narray2 = ret.T
print('\n转置矩阵：\n', narray2)
"""
 [[0 2 4]
 [1 3 5]]
"""
