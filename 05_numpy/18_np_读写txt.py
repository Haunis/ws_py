"""
读写txt文件：
np.savetxt("../tmp/arr.txt", arr, fmt = "%d", delimiter = ",")
    是将数组以 整型 ，逗号分割写入文件

 np.genfromtxt("../tmp/arr.txt", delimiter = ",")是结构化数组和缺失数据。没明白，日后再理解理解

"""

import numpy as np

a = np.arange(0, 12, 0.5).reshape(4, -1)
np.savetxt("a1.txt", a)

# 把文件加载到一个二维数组中； 默认按照'%.18e'格式保存数值
ret = np.loadtxt("a1.txt")
print(ret)

print("------保存整数-------")
# 改为保存为整数，以逗号分隔
np.savetxt("a2.txt", a, fmt="%d", delimiter=",")
ret = np.loadtxt("a2.txt", delimiter=",")
print(ret)

ret = np.genfromtxt("a2.txt", delimiter=",")
print("genfromtxt:\n", ret)
