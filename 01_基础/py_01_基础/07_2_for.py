"""
range()在python2和python3区别：
    python2返回列表对象，python3返回的是迭代器(可迭代对象)

"""

print("------------------1.普通for循环--------------------")
list_name = ["ann", "lee", "wang"]
for item in list_name:
    print(item)

print("------------------2.完整for循环--------------------")
for item in list_name:
    print(item)
    break;
else:
    # for循环遍历完成,且未使用break方可执行else里的内容
    print("execute else")

print("------------------3.range--------------------")
for i in range(10): #0～9
    print(i)

print("------------------4.range--------------------")
for i in range(5, 10):  # 5,6,7,8,9 --5开始，10结束(不包括10)，步长是1
    print(i)

print("------------------5.range--------------------")
for i in range(5, 10, 2):  # 5,7,9 --5开始，10结束(不包括10)，步长是2
    print(i)
