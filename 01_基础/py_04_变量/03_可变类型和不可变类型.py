"""
可变和不可变类型的概念:
    当改变变量内容时,变量引用发生改变就是不可变类型;反之就是可变类型
不可变类型
    1.数字类型 int float bool complex long(2.x)
    2.字符串
    3.元组
可变类型: 列表, 字典
"""

list_num = [1, 2, 3]
print(id(list_num))
list_num.append(999)
print(id(list_num))  # 地址不变
