"""
生成随机ndarray
    np.random.randint(low, high = None, size = None)

"""
import numpy as np

print("------------1.randint------------------")
narray = np.random.randint(0, 3, (3, 4))  # 返回ndarray；生成3*4矩阵,元素随机是[0,3)
print(narray)


print("\n------------2.rand------------------")
narray = np.random.rand(3, 4)
print(narray)

print("\n------------3.randn------------------")
narray = np.random.randn(3, 3)  # 随机正太分布
print(narray)

print("\n------------4.normal------------------")
narray = np.random.normal(size=(3, 3))
print(narray)

print("\n------------5.uniform------------------")
narray = np.random.uniform(0, 20, 5)  # ndarray;从一个均匀分布中随机采样[0,20),采取5个
print(narray)
