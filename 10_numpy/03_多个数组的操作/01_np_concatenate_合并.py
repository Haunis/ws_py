"""
hstack()：横向合并,就是横向扩张
vstack()：纵向合并,就是纵向扩张
concatenate(tuple,axis=1):axis=0时纵向合并,axis=1时进行横向合并

"""
import numpy as np

narray1 = np.arange(8).reshape(4, 2)
narray2 = narray1 * 2
# narray3 = np.vstack((narray1, narray2))
# narray3 = np.hstack((narray1, narray2))

narray3 = np.concatenate((narray1, narray2), axis=0)  # 0--纵向扩张;1--横向扩张

print("\nret1:\n", narray1)
print("\nret2:\n", narray2)
print("\nret3:\n", narray3)
