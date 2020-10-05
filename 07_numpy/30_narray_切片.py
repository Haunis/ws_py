"""
一维数组的切片,和Python中的切片一样

多维数组的切片,相当于matlab里取矩阵的子矩阵
    arr[arg1,arg2] #如果arg1和arg有一个是单列或者单行,返回结果是一维数组;否则返回二维数组
"""

import numpy as np

print("----------------1.一维数组的切片---------------")
arr = np.arange(10)
print(arr)
print(arr[2])
print(arr[-1])
print(arr[1:4])

print("\n----------------2.多维数组的切片---------------")
arr = np.arange(12).reshape(3, 4)
print(arr)
print("arr[0, 1:3] : ", arr[0, 1:3])  # 二维;索引第0行中第1列到第2列的元素(不包含第三列)
print("arr[:,2]: ", arr[:, 2])  # 二维;索引第2列元素,和matlab一样
print("arr[:1, :1]= ", arr[:1, :1])  # 二维; 第0行第0列元素(0:1行不包含1,0:1列不包含1)
print("arr[1:3, 3]:", arr[1:3, 3])  # 一维:第[1,3)行,第3列

print("----------------")
arr = np.arange(12).reshape(3, 4)
print(arr)

# 从两个序列的对应位置取出两个整数来组成下标：arr[0,1],arr[1,3]
# 相当于arr[arr[0,1],arr[1,3]]
print('索引结果1：', arr[(0, 1), (1, 3)])  # 一维

print('索引结果2：', arr[1:2, (0, 2, 3)])  # 返回二维;索引第1到2行,第0、2、3列的元素

mask = np.array([1, 0, 1], dtype=np.bool)  # mask是一个布尔数组
print('索引结果3：', arr[mask, 1])  # 一维; 索引第0,2行中第1列元素
