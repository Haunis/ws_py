"""
轴对换
参考:https://blog.csdn.net/qq1483661204/article/details/70543952
"""
import numpy as np

narray1 = np.arange(8).reshape(4, 2)
print("\n原始数据:\n", narray1)

narray2 = narray1.swapaxes(0, 1)
print("\nnarray2：\n", narray2)

print("\ntranspose:\n", narray1.transpose((1, 0)))
