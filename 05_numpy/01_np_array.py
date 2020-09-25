"""
np.array(object, dtype,ndmin) #返回numpy.ndarray
    object: 接收python中list,tuple
    dtype: 元素元素类型,未指定则选择保存所需的最小类型,默认None
    ndim: 接收int,制定生成数组应该具有的最小维数，默认为None

ndarray是一个通用的同构数据容器，即其中的所有元素都需要相同的类型
课程说的是多维数组,在线性代数角度来说就是矩阵
属性说明
    ndim 	返回数组的轴的个数
    shape	返回数组的维度,比如(2,3) 就是2*3矩阵的意思
    size	返回数组元素个数
    dtype	返回数据类型
    itemsize	返回数组中每个元素的字节大小




"""

import numpy as np

print("-------------1.接收列表------------------")
data1 = [1, 3, 5, 7]  # 列表
print("data1:", data1)
w1 = np.array(data1)
print('w1:', w1)  # 和data1输出结果不同,data1输出结构有逗号
print(type(w1))  # numpy.ndarray
print("w1.dtype:", w1.dtype)  # int64
print("w1[0]:", w1[0])  # 直接获取一维数组里的元素

print("\n-------------2.接收列表------------------")
data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]  # 多维数组
w3 = np.array(data3)
print('w3:', w3)

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
print('ret:', ret)
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
