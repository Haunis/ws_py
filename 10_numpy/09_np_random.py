"""
生成随机ndarray
    np.random.randint(low, high = None, size = None)

"""
import numpy as np

print("------------1.randint------------------")
ret = np.random.randint(0, 3, (3, 4))  # 生成3*4矩阵,元素随机是[0,3)
print(ret)
print("type(ret):", type(ret))  # ndarray

print("\n------------2.rand------------------")
ret = np.random.rand(3, 4)
print(ret)

print("\n------------3.randn------------------")
ret = np.random.randn(3, 3)  # 随机正太分布
print(ret)

print("\n------------4.normal------------------")
ret = np.random.normal(size=(3, 3))
print(type(ret))
print(ret)