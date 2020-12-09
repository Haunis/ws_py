"""
用法1：
    np.where(condition,x,y)
        condition True输出x,否则输出y
        condition 为列表的话，x,y也应该为对应纬度
用法2：
    np.where(narray > 3)
        返回narray 中大于3的元素的索引
"""

import numpy as np

print("\n----------------1.正常使用----------------")

# 条件为[[True, True], [False, False]]，分别对应最后输出结果的四个值
# 第一个值从[1,5]中选，因为条件为True，所以是选1。
# 第二个值从[2,6]中选，因为条件为True，所以选6，后面以此类推。
narray_ret1 = np.where([[True, True], [False, False]], [[1, 2], [3, 4]], [[5, 6], [7, 8]])  # ok
print("\nnarray_ret1:\n", narray_ret1)

narray_bool = np.array([[True, True], [False, False]])
narray_ret2 = np.where(narray_bool, [[1, 2], [3, 4]], [[5, 6], [7, 8]])
print("\nnarray_ret2:\n", narray_ret2)

narray1 = np.array([[1, 2], [3, 4]])
narray2 = np.array([[5, 6], [7, 8]])
narray_ret3 = np.where(narray_bool, narray1, narray2)  # 满足条件从narray1选，否则从n2rray2选;返回ndarray
print("\narray_ret3:\n", narray_ret3)

print("\n----------------2.只有condition----------------")
narray = np.array([0, 10, 20, 30, 40, 50, 60])
my_tuple = np.where(narray > 30)  # 返回一个元组，原数组有几维，tuple中就包含几个数组，数组中保存元素坐标
print(my_tuple)  # (array([4, 5, 6]),) ，保存的是索引
