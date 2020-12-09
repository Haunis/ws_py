"""
vsplit():竖着分上下两部分,纵向减少
hsplit():横着分左右两部分,横向减小

numpy.split(narray,num,axis=0)
    返回列表，列表里存多维数组
    num:分成几部分
    axis: 0--竖直方向分上下两部分；1--水平方向分左右两部分
"""
import numpy as np

narray = np.arange(12).reshape(6, 2)
print("oringin data:\n", narray)

# li = np.vsplit(narray, 2)# 竖直方向分成2部分,li是保存2个narray的list
li = np.hsplit(narray, 2)  # 水平方向分成2部分,li是保存2个narray的list;
# li = np.split(narray, 2, axis=0)  # 返回list; 竖着分两部分

print("\n切割后 narray2:\n", li)
print("\nli[0]:\n", li[0])  # 切割后，子narray还是多维数组
"""
li[0]:
 [[ 0]
 [ 2]
 [ 4]
 [ 6]
 [ 8]
 [10]]
"""
