"""
narray拷贝出一份新数据
切片返回的是原始数组的视图,若需要非视图则可复制数据出来
"""
import numpy as np

narray = np.arange(10)
# narray2 = narray[-4:-1].copy()
narray2 = np.copy(narray[-4:-1])
print("narray:", narray)  # [0 1 2 3 4 5 6 7 8 9]
print("narray2:", narray2)  # [6 7 8]

