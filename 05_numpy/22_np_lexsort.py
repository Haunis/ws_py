"""
lexsort(keys, axis=None)
    key:array 或者 元组
    返回值是按照最后一个传入数据排序的nrray
"""

import numpy as np

a = np.array([7, 2, 1, 4])
b = np.array([5, 2, 6, 7])
c = np.array([5, 2, 4, 6])
ret = np.lexsort((a, b, c))  # narray
print("ret:", ret)
print("a[ret]:", a[ret])

ret2 = zip(a[ret], b[ret], c[ret])  # 将可迭代对象打包成一个个元组,返回zip对象
# print("list(ret2):\n", list(ret2))
print('list(zip(*ret2))\n', list(zip(*ret2)))  # zip(*ret2) 相当于解压
