"""
np.where(condition,x,y)
    condition True输出x,否则输出y
    condition为多为数组的话，x,y也应该为对应纬度

"""

import numpy as np

print("\n----------------1.正常使用----------------")
condition = np.array([[True, False], [True, True]])

# 条件为[[True,False], [True,False]]，分别对应最后输出结果的四个值，运算时第一个值从[1,9]中选，
# 因为条件为True，所以是选1。第二个值从[2,8]中选，因为条件为False，所以选8，后面以此类推。
# ret = np.where([[True, False], [True, True]], [[1, 2], [3, 4]], [[9, 8], [7, 6]]) #ok
# ret = np.where(condition, [[1, 2], [3, 4]], [[9, 8], [7, 6]])
value1 = np.array([[1, 2], [3, 4]])
value2 = np.array([[9, 8], [7, 6]])
ret = np.where(condition, value1, value2) #满足条件从value1选，否则从value2选
print(ret)

print("\n----------------2.只有condition----------------")
ret = np.array([2, 5, 6, 3, 10])
ret = np.where(ret > 4)  # 返回一个元组，原数组有几维，tuple中就包含几个数组，数组中保存元素坐标
print(type(ret))  # 元组
print(ret)
