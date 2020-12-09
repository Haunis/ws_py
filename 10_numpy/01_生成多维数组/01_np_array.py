"""
np.array(object, dtype,ndmin) #返回numpy.ndarray
    object: 接收python中list,tuple
    dtype: 元素元素类型,未指定则选择保存所需的最小类型,默认None
    ndim: 接收int,制定生成数组应该具有的最小维数，默认为None

ndarray:多维数组;是一个通用的同构数据容器，即其中的所有元素都需要相同的类型

属性说明
    ndim 	返回数组的轴的个数
    shape	返回数组的维度,比如(2,3) 就是2*3矩阵的意思
    size	返回数组元素个数
    dtype	返回数据类型
    itemsize	返回数组中每个元素的字节大小

"""

import numpy as np
import pandas as pd

print("-------------1.接收列表------------------")
li = [1, 3, 5, 7]  # 列表
print("li:", li)
ret = np.array(li)
print('ret:', ret)  # 和data1输出结果不同,data1输出结构有逗号
print(type(ret))  # numpy.ndarray
print("ret.dtype:", ret.dtype)  # int64
print("w1[0]:", ret[0])  # 直接获取一维数组里的元素
print("ret.shape:", ret.shape)  # (4,)

print("\n-------------2.接收列表------------------")
data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]  # 多维数组
ret = np.array(data3)
print('ret:\n', ret)

print("\n-------------3.接收元组------------------")
data2 = (2, 4, 6, 8)  # 元组
w2 = np.array(data2)
print('w2:', w2)

print("\n-------------4.指定数据类型------------------")
w = np.array([1.2, 3, 4, 4], dtype='float64')
print('w:', w)
print("w.dtype: ", w.dtype)  # float64

print("\n-------------5.ndarray属性说明------------------")
ret = np.array([[1, 2, 3], [4, 5, 6]])
print('ret:\n', ret)
print('秩为：', ret.ndim)  # 2
print('形状为：', ret.shape)  # (2,3) 即2*3矩阵
print('元素个数为：', ret.size)  # 6,即一共多少个是元素

ret.shape = (3, 2)  # 将矩阵设置为3*2矩阵
print(ret)

print(">>astype<<")
ret2 = ret.astype(np.float64)  # 生成一个新类型矩阵;原矩阵ret类型不变
print(ret2)

print("\n-------------6.ndarray和标量的运算------------------")
ret = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(ret)
ret = ret * 100
print(ret)

print("\n-------------7.布尔选择------------------")
narray = np.array([1, 2, 3, 4])
bool_narray = narray > narray.mean()
se = pd.Series(bool_narray)

print("bool_narray:", bool_narray)  # [False False  True  True]
print(narray[bool_narray])  # [3 4]
print(narray[se])  # [3 4]和上述结果一样
