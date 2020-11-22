"""
读写二进制文件：
    读：ret = np.load("xxx_file")
    写：np.save("file",x,y) 可以保存一个数组，也可以保存多个数组
"""

import numpy as np

print("\n--------------1.save单个数组--------------------")
nda = np.arange(1, 13).reshape(3, 4)
np.save('arr.npy', nda)  # np.save("arr", nda)

ret_nda = np.load('arr.npy')
print("\nafter load ret_nda:\n",ret_nda)


print("\n--------------2.save多个数组--------------------")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)  # 长度为10

print("save...")
print("\na:\n", a)
print("\nb:\n", b)
print("\nc:\n", c)
np.savez('result.npz', a, b, sin_array=c)

print("\nload...")
r = np.load('result.npz')
print("\nr:", r)  # NpzFile类型
a = r['arr_0']  # 数组a
print(a)
