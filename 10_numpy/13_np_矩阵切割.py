"""
和矩阵合并相反
hsplit():竖着切一刀
vsplit():横着切一刀
split(narray,num,axis=0):指定方向切割; 0--横着切一刀,1--竖着切一刀
"""
import numpy as np

ret = np.arange(16).reshape(4, 4)
print("oringin data:\n",ret)

# ret2 = np.hsplit(ret, 2)  # 水平方向分成2部分,ret2是保存2个narray的narray
# ret2 = np.vsplit(ret, 2)
ret2 = np.split(ret, 2, axis=0)  # 竖着分两部分

print("\n切割后")
print("ret2:\n", ret2)
print("\nret2[0]:\n", ret2[0])
print("\nret2[0][0][1]:\n", ret2[0][0][1])  # ret2第0个narray中的第0个narray(一维)中的第1个元素
