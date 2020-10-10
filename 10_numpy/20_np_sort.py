"""
sort函数对数据直接进行排序，调用改变原始数组，无返回值。
numpy.sort(a, axis, kind, order)
如果a是多维数组则对数组所有行或所有列进行排序
    参数说明:
        a:要排序的数组
        kind: 排序算法，默认为“quicksort”
        order: 排序的字段名，可指定字段排序，默认为None
        axis: 指定轴对数据集进行排序.
               axis=1为沿横轴排序；
               axis=0为沿纵轴排序；
               axis=None,将数组平坦化之后进行排序
"""
import numpy as np

arr = np.array([7, 9, 5, 2, 9, 4, 3, 1, 4, 3])
print('原数组：', arr)
arr.sort()
print('排序后：', arr)

print("\n-------------指定axis----------------")
arr = np.array([[4, 2, 9, 5], [6, 4, 8, 3], [1, 6, 2, 4]])
print('原数组：\n', arr)
arr.sort(axis=1)  # 沿横向排序
print('横向排序后：\n', arr)
