"""
改变矩阵的形状,如使用2*4矩阵生成4*2的矩阵:
    方式1: narray.reshape(2,4) #生成新矩阵,旧矩阵不变
    方式2: np.reshape(narray,(2,4)) #生成新矩阵,旧矩阵不变
    两个参数中的一个可以为-1,表示自动推断
reshape()可以将数组设置成多个纬度,现不考虑那么多,只考虑2个纬度
"""

import numpy as np

nda = np.arange(8)
print("origin data:", nda)

print("\n---------------1.narray.reshape()------------------")
nda2 = nda.reshape(2, 4)  # 生成2*4新矩阵,原矩阵ret不变
print("nda2:\n", nda2)

print("\n---------------2.np.reshape()------------------")
nda2 = np.reshape(nda, (4, 2))  # 生成4*2矩阵,原矩阵ret不变
nda2 = np.reshape(nda, (4, -1))  # 自动推断矩阵的列数
print("nda2:\n", nda2)

print("---------")
# ndarray中有2个ndarray-a,这2个ndnarray-a中各有2个子ndnarray-b,ndnarray-b,含有4个元素
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
