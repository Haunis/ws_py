"""
生成随机矩阵
np.random.randint(low, high = None, size = None)

"""
import numpy as np

print("------------1.randint------------------")
ret = np.random.randint(0, 3, (3, 4)) #生成3*4矩阵,元素随机是[0,3)
print(ret)
print("type(ret):", type(ret))

print("\n------------2.rand------------------")
ret = np.random.rand(3,4)
print(ret)