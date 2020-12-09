"""
改变数组的形状,如使用2*4转换为4*2的数组:
    方式1: narray.reshape(2,4) #生成新数组,旧数组不变
    方式2: np.reshape(narray,(2,4)) #生成新数组,旧数组不变
    两个参数中的一个可以为-1,表示自动推断
reshape()可以将数组设置成多个纬度,现不考虑那么多,只考虑2个纬度
"""

import numpy as np

narray = np.arange(8)
print("origin data:", narray)

print("\n---------------1.narray.reshape()------------------")
narray1 = narray.reshape(2, 4)  # 生成2*4新矩阵,原矩阵ret不变
print("narray1:\n", narray1)

print("\n---------------2.np.reshape()------------------")
# narray2 = np.reshape(narray, (4, 2))  # 生成4*2矩阵,原矩阵ret不变
narray2 = np.reshape(narray, (4, -1))  # 自动推断矩阵的列数
print("narray2:\n", narray2)

print("\n--------------3.np.reshape()多维--------------")
# ndarray中有2个ndarray-a,这2个ndnarray-a中各有2个子ndnarray-b,ndnarray-b,含有4个元素
narray3 = np.reshape(np.arange(16), (2, 2, 4))
print(narray3)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]
"""
print("narray3[1][0][3]:", narray3[1][0][3])  # 11
