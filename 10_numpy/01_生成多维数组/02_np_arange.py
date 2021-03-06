"""
创建一维等差数组
np.arange([start,] stop, [step,] dtype)
返回 numpy.ndarray
    start:	起始值，默认从0开始;
    stop: 	结束值；<<<<<生成的元素不包括结束值>>>>>
    step	步长，可省略，默认步长为1；
    dtype 	设置元素的数据类型，默认使用输入数据的类型。
"""

import numpy as np

print("--------------1.只传一个参数-------------------")
narray = np.arange(10)  # 返回numpy.ndarray
print(narray)  # [0 1 2 3 4 5 6 7 8 9]

print("\n--------------2.传start,stop,step-------------------")
narray = np.arange(0, 10, 1)  # 包左不包右
print(narray)  # [0 1 2 3 4 5 6 7 8 9]
