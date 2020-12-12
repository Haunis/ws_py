"""
ndarray.shape : 返回一个元组
    如果元组是一个元素，代表数组ndarray是个一维数组
    否则是个多维数组
"""
import numpy as np

print("----------1.一维数组-----------")
nda = np.arange(0, 24)
print("shape:", nda.shape)  # (24,) 返回一个元组
print(nda)

print("\n----------2.二维数组-----------")
nda = np.arange(0, 24).reshape(2, 12)
print("shape:", nda.shape)  # (2, 12)
print(nda)

print("\n----------3.三维数组-----------")
nda = np.arange(0, 24).reshape(2, 3, 4)
print("shape:", nda.shape)  # (2, 3, 4)
print(nda)
