"""
轴对换
参考:https://blog.csdn.net/qq1483661204/article/details/70543952
"""
import numpy as np
ret = np.arange(6).reshape(3,2)
print(ret)
print(ret.swapaxes(0,1))

print("---")
# print(ret)
print(ret.transpose((1,0)))