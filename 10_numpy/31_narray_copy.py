"""
narray拷贝出一份新数据
切片返回的是原始数组的视图,若需要非视图则可复制数据出来
"""
import numpy as np

arr = np.arange(10)
arr1 = arr[-4:-1].copy()
print(arr)
print(arr1)
