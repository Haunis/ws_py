"""
hstack()：横向合并,就是横向扩张
vstack()：纵向合并
concatenate(tuple,axis=1):axis=0时纵向合并,axis=1时进行横向合并

"""
import numpy as np

ret1 = np.arange(6).reshape(3, 2)
ret2 = ret1 * 2
# ret3 = np.hstack((ret1, ret2))
# ret3 = np.vstack((ret1, ret2))
ret3 = np.concatenate((ret1, ret2), axis=0)  # 0--纵向合并;1--横向合并

print("ret1:\n", ret1)
print("ret2:\n", ret2)
print("ret3:\n", ret3)
