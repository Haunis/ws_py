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
