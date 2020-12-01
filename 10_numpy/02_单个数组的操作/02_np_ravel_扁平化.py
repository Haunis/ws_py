"""
ravel: “解开”的意思
将矩阵扁平化:
    就是变成一维数组
    方式1: narray.ravel()
    方式2: numpy.ravel(narray)

"""
import numpy as np

narray = np.reshape(np.arange(8), (2, 4))
print("before 扁平化:\n", narray)

# ret2 = ret.ravel()
narray2 = np.ravel(narray)  # 将矩阵扁平化生成新矩阵,原矩阵不变
print("\nafter 扁平化:\n", narray2)
