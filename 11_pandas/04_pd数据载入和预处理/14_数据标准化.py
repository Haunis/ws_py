"""
参考:https://www.cnblogs.com/yahengwang/p/10634010.html
离差标准化:
    对原始数据所做的一种线性变换，将原始数据的数值映射到[0,1]区间
    公式:x1=(x−min)⁄(max−min)

标准差标准化:
    又称零均值标准化或z分数标准化，是当前使用最广泛的数据标准化方法
    经过处理的数据符合标准正态分布，即均值为0，标准差为1
    公式:x1=(x−mean)⁄std

"""
import numpy as np

np.set_printoptions(precision=3)

print("--------------1.数据的离差标准化-------------------")


def MinMaxScale(data):
    data = (data - data.min()) / (data.max() - data.min())
    return data


x = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])
print('原始数据为：\n', x)
x_scaled = MinMaxScale(x)
np.set_printoptions(precision=2)  # 输出时,小数点保留两位
print('标准化后矩阵为:\n', x_scaled, end='\n')

print("\n--------------2.数据的标准差标准化-------------------")


def StandardScale(data):
    data = (data - data.mean()) / data.std()
    return data


x = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])
print('原始数据为：\n', x)
x_scaled = StandardScale(x)
print('标准化后矩阵为:\n', x_scaled, end='\n')
