"""
读写二进制文件：
    读：ret = np.load("xxx_file")
    写：np.save("file",x,y) 可以保存一个数组，也可以保存多个数组
       np.savez('./binary_mul_narray.npz', a, b, sin_array=c)
"""

import numpy as np

print("\n--------------1.save单个数组--------------------")
narray = np.arange(12).reshape(3, 4)
print("save:\n", narray)
np.save('./binary.npy', narray)

narray_load = np.load('./binary.npy')
print("\nload>>> ret_nda:\n", narray_load)

print("\n--------------2.save多个数组--------------------")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)  # 长度为10
print("save:")
print("a:\n", a)
print("b:\n", b)
print("c:\n", c)
np.savez('./binary_mul_narray.npz', a, b, sin_array=c)

npz_load = np.load('./binary_mul_narray.npz')  # numpy.lib.npyio.NpzFile
print("\nload>>> npz_load:", npz_load)  # <numpy.lib.npyio.NpzFile object at 0x7fe184233f40>
narray_0 = npz_load['arr_0']  # 数组a
print("narray_0:\n", narray_0)
