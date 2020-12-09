"""
读写txt文件：
np.savetxt("../tmp/arr.txt", arr, fmt = "%d", delimiter = ",")
    是将数组以整型 ，逗号分割写入文件

np.loadtxt("../tmp/arr.txt",delimiter = ",")把文件加载到一个二维数组中；

np.genfromtxt("../tmp/arr.txt", delimiter = ",")是结构化数组和缺失数据。没明白，日后再理解理解

"""

import numpy as np

print("\n-----------1.默认保存-----------")
nda = np.arange(0, 12, 0.5).reshape(4, -1)  # ndarray
np.savetxt("a1.txt", nda)  # 默认按照'%.18e'格式保存数值

nda_load = np.loadtxt("a1.txt")  # 把文件加载到一个二维数组中
print("nda_load:\n", nda_load)

print("\n-----------2.指定格式保存-----------")
np.savetxt("a2.txt", nda, fmt="%d", delimiter=",")  # fmt指定为整数，delimiter指定为逗号
nda_load = np.loadtxt("a2.txt", delimiter=",")
print("nda_load:\n", nda_load)

print("\n-----------3.genfromtxt()-----------")
nda_gen = np.genfromtxt("a2.txt", delimiter=",")  # ndarray
print("nda_gen:\n", nda_gen)
