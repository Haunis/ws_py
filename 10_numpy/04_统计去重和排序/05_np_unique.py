"""
np.uniques(narray)
    对于一维数组或者列表,去除其中重复的元素，并按元素由大到小返回一个新的元组或者列表
    对narray多维数组去重,最终返回一维narray
"""
import numpy as np

print("-----------1.一维数组去重------------")
names = np.array(['r', 'g', 'b', 'w', 'w'])
print('原数组：', names)  # ['r' 'g' 'b' 'w' 'w']

ret = np.unique(names)  # ['b' 'g' 'r' 'w']
print('去重后：', ret)

print("\n-----------2.二维数组去重------------")

nda = np.random.randint(1, 10, (4, 4))  # 生成4*4数组，数字从[1,10)选
print("原数组：\n", nda)
nda2 = np.unique(nda)  # 返回一维的narray
print("去重后:", nda2)
