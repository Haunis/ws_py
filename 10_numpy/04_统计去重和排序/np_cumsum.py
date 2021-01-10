"""
轴向元素累加和

ndarray.cumsum(axis)
    axis: None 所有元素累加
    axis: 0 纵向
    axis: 1 横向
"""
import numpy as np

nda = np.arange(30).reshape(3, 10)
ret_none = nda.cumsum(None)
ret_0 = nda.cumsum(0)
ret_1 = nda.cumsum(1)
print("原始数据:\n", nda)
print("\nret_none:\n", ret_none)
print("\nret_0 纵向:\n", ret_0)
print("\nret_1 横向:\n", ret_1)
