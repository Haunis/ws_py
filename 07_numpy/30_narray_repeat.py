"""
narray.repeat(A, reps, axis = None)
    A: 是需要重复的数组元素
   repeats: 是重复次数，
   axis: 指定沿着哪个轴进行重复，
        axis = 0,纵向重复 ,和matlab一样默认0,进行列行为
        axis = 1,横向重复

另外还有 np.tile(A, reps)可进行重复操作
"""

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
ret_repeat = arr.repeat(2, axis=0)
print('原数组:\n', arr)
print('ret_repeat：\n', ret_repeat)
