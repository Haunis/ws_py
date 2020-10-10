"""
获取矩阵的转置矩阵:
    方式1:np.transpose(narray,(1,0))
    方式2:narray.transpose((1,0)) #注意参数是元组
    方式3:narray.T #使用narray的T属性获取转置矩阵
"""

import numpy as np

ret = np.arange(6).reshape(3, 2)
print(ret)

ret2 = np.transpose(ret, (1, 0))
# ret2 = ret.transpose((1, 0))
# ret2 = ret.T
print('转置矩阵：\n', ret2)
