"""
ufunc:
    通用函数，是一种能够对数组中的所有元素进行操作的函数。
    对一个数组进行重复运算时，使用ufunc函数比使用math库中的函数效率要高很多

常用的ufunc函数运算有四则运算、比较运算和逻辑运算。
    四则运算：
        +,0,*,/,**(幂运算)。数组间的四则运算表示对每个数组中的元素分别进行四则运算，所以形状必须相同。
    比较运算：
        >、<、==、>=、<=、!=。比较运算返回的结果是一个布尔数组，每个元素为每个数组对应元素的比较结果。

广播（broadcasting）是指不同形状的数组之间执行算术运算的方式。需要遵循4个原则：
    1.让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在左边加1补齐。
    2.如果两个数组的形状在任何一个维度上都不匹配，那么数组的形状会沿着维度为1的维度进行扩展
        ，以匹配另一个数组的形状。
    3.输出数组的shape是输入数组shape的各个轴上的最大值。
    4.如果两个数组的形状在任何一个维度上都不匹配，并且没有任何一个维度等于1，则引发异常


"""
import numpy as np

print("---------------1.四则运算-----------------")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("x:", x)
print("y:", y)
print('数组相加结果：', x + y)
print('数组相减结果：', x - y)
print('数组相乘结果：', x * y)
print('数组幂运算结果：', x ** y)

print("\n-------------2.比较运算-----------------")
x = np.array([1, 3, 6])
y = np.array([2, 3, 4])
print("x:", x)
print("y:", y)
print('比较结果(<)：', x < y)  # 返回bool类型的narray
print('比较结果(>)：', x > y)
print('比较结果(==)：', x == y)
print('比较结果(>=)：', x >= y)
print('比较结果(!=)：', x != y)

print("\n-------------3.逻辑运算-----------------")
arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([2, 4, 6, 8])
cond = np.array([True, False, True, False])

# 该方法对大规模数据处理效率不高，也无法用于多维数组，where可以克服这个
# c为True返回x,否则返回y
result = [(x if c else y) for x, y, c in zip(arr1, arr2, cond)]
print(result)

print("\n-------------4.ufunc函数广播-----------------")
arr1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
arr2 = np.array([1, 2, 3])
print('arr1:\n', arr1)
print('arr2:\n', arr2)
print('arr1+arr2:\n', arr1 + arr2)

a = np.arange(1, 13).reshape(4, 3)
b = np.arange(1, 5).reshape(4, 1)
print(a)
print(b)
print(a + b)  # a的每一行都就加上b

print("------")
a = np.arange(1, 13).reshape(4, 3)
b = np.arange(1, 5).reshape(4, 1)
print(a)
print(b)
print(a + b)  # a的每一列都加上b
