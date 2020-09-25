"""
将矩阵扁平化:
    方式1: narray.ravel()
    方式2: numpy.ravel(narray)

"""
import numpy as np

ret = np.arange(8)
ret = np.reshape(ret, (2, 4))
print(ret)

# ret2 = ret.ravel()
ret2 = np.ravel(ret)  # 将矩阵扁平化生成新矩阵,原矩阵不变
print(ret2)
