#!/usr/bin/python3
"""

和列表的区别：
    1.使用括号"()"定义
    2.元组中的元素不可修改
关于元组注意事项:
    1.元组里的元素无法修改,但元组里可以存储变量，如list
    2.定义元组可以不带括号
    3.元组只有一个元素时，要在元素末尾加上逗号，否则括号会被当成运算符处理
    4.元组的遍历不常见;
    5.通常元组保存的数据类型是不同的

元组应用场景:
    1.作为函数的参数或者返回值; 作函数参数可以接收任意多个参数,作为返回值可以返回多个
    2.格式字符串; 格式化字符串后面的()本质上就是一个元组
    3.保护数据安全,元组中的元素不可被修改

"""
print("-------------1.普通元组------------------")
info_tuple = ("lee", 27, 178)
info_tuple = "lee", 28, 177  # 定义元组可以不带括号()
print("info_tuple(0) = %s" % info_tuple[0])

print("-------------2.定义空元组------------------")
empty_tuple = ()
print("type(empty_tuple) = %s" % type(empty_tuple))

print("-------------3.定义只包含一个元素的元组----------------")
single_tuple = ("lee",)  # 如果不带逗号，single_tuple是int类型
print("type(single_tuple):%s" % type(single_tuple))

print("-------------4.index----------------")
print("info_tuple.index(28) : %d" % info_tuple.index(28))  # 28所在的索引
print("len(info_tuple):%d" % len(info_tuple))  # 元组的长度

print("--------------5.遍历------------------")
for my_info in info_tuple:
    print(my_info)

print("--------------6.格式化字符串------------------")
person_tuple = ("xiao_ming", 22, 175)
print("name=%s, age=%d, height=%d" % person_tuple)  # person_tuple就是个元组
str_tuple = "name=%s, age=%d, height=%d" % person_tuple
print(str_tuple)

print("--------------7.元组和列表之间相互转换------------------")
num_list = [1, 2, 3, 4]
tuple_list = tuple(num_list)  # 列表转换为元组

num_list2 = list(tuple_list)  # 元组转换为列表
print("type(num_list) : %s" % type(num_list))
print("type(tuple_list) : %s" % type(tuple_list))
print("type(num_list2) : %s" % type(num_list2))
