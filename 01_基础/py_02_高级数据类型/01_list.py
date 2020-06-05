"""
就是数组
使用 += 实际上是调用了列表的extend()方法

创建空列表: empty_list = []
"""

name_list = ["lee0", "lee1", "lee2"]  # 在python3解释器程序中输入name_list.按tab键会有提示可以使用哪些方法
print("name_list : %s " % name_list)

print("--------------1.取值和取索引---------------------")
print("name_list[0] = %s" % name_list[0])  # 取值时候,角标不能超过列表大小
print("name_list.index(\"lee2\") = %d" % name_list.index("lee2"))

print("--------------2.修改---------------------")
# 修改数组中的内容
name_list[0] = "wang00"
print("name_list[0] = %s" % name_list[0])

print("--------------3.增加---------------------")
name_list.append("append0")  # 添加一个元素,如果添加的是个列表,就把列表当做一个元素
name_list.insert(0, "insert0")
name_list2 = ["su0", "su1", "su2"]
name_list.extend(name_list2)  # 扩展列表
print(name_list)

print("--------------4.删除---------------------")
name_list.remove("lee2")  # 如果列表中有多个相同的元素,删除第一个出现的
name_list.pop()  # 默认删除最后一个
name_list.pop(0)
del name_list[1]  # del 是把一个变量从内存中删除的,删除后变量不可继续使用,日常开发中不使用

name_list.clear()
print(name_list)
print("--------------5.len和count---------------------")

book_list = ["android", "ios", "python", "java", "python"]
print("book_list : %s" % book_list)
book_list_len = len(book_list)
print("列表的长度 len(book_list)=%s" % book_list_len)

python_count = book_list.count("python")
print("python 出现的次数 :%d " % python_count)

print("--------------6.排序---------------------")
animal_list = ["cat", "pig", "dog", "fish"]
print("origin animal_list = %s " % animal_list)
# animal_list.sort()#升序
animal_list.sort(reverse=True)  # 降序
print("after animal_list = %s " % animal_list)

print("--------------7.反转---------------------")
reverse_list = ["aa", "bb", "cc", "dd"]
reverse_list = ["aa", "bb", "cc", "dd"]
print("reverse_list = %s" % reverse_list)
reverse_list.reverse()
print("reverse_list = %s" % reverse_list)

print("--------------8.遍历---------------------")
for var in reverse_list:
    print(var)

for temp in enumerate(reverse_list):
    print(temp)  # temp是个元组
for i, value in enumerate(reverse_list):  # 使用i value接收，拆包
    print(i, value)
