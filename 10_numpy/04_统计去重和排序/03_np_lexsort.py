"""
参考:https://blog.csdn.net/yu_1628060739/article/details/102680203
lexsort(keys, axis=None)
    key:array 或者 元组
    返回值是按照最后一个传入数据排序的索引
"""

import numpy as np

a = np.array([7, 2, 1, 4])
b = np.array([5, 2, 6, 7])
c = np.array([5, 2, 4, 6])  # c是最后传入的,按c进行排序;
ret_nda = np.lexsort((a, b, c))  # narray

print("ret_nda:", ret_nda) # [1 2 0 3]
print("c[ret_nda]:", c[ret_nda])

ret_zip = zip(a[ret_nda], b[ret_nda], c[ret_nda])  # 将可迭代对象打包成一个个元组,返回zip对象
# print("list(ret_zip):\n", list(ret_zip))

print('list(zip(*ret_zip))\n', list(zip(*ret_zip)))  # zip(*ret_zip) 相当于解压
