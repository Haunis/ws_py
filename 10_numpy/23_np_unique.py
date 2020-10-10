"""
np.uniques(narray)
    对于一维数组或者列表,去除其中重复的元素，并按元素由大到小返回一个新的元组或者列表
    对narray多维数组去重,最终返回一维narray
"""
import numpy as np

names = np.array(['红色', '蓝色', '黄色', '白色', '红色'])
print('原数组：', names)

ret = np.unique(names)
print('去重后：', ret)

ret = np.random.randint(1, 100, (4, 4))
print(ret)
ret2 = np.unique(ret)  # 返回一维的narray
print(type(ret2))
print("去重后:", ret2)
