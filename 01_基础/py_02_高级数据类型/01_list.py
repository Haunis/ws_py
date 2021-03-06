"""
就是数组
使用 += 实际上是调用了列表的extend()方法

创建空列表: empty_list = []或者 empty_list = list()

列表切片可以进行替换和删除动作
如: list[0:3] = [1,2,3,4,5,6] #替换
    del list[0:3] #删除列表0,1,2元素

切片返回的是一个新的列表
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

print("--------------9.range---------------------")
temp_list = range(10)  # 返回range对象,什么时候取,什么时候生成,节省内存
print(temp_list[3])  # 第四个元素

print("--------------10.列表推导式---------------------")
temp_list2 = [x for x in range(10)]  # 返回的是个列表
print("type(temp_list) : ", type(temp_list2))
print(temp_list2)

print("\n--------------11.切片---------------------")
li = [i/2 for i in range(24)]
print("origin:", li)

print("li[::3]:", li[::3])  # 每隔3个取一个
