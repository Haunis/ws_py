"""
eval(str): 将字符串转为表达式

注意事项: 不要使用eval()直接转换input的结果
    如 eval("__import__('os').system('rm aaa')")
    等价于:
    import os
    os.system("rm aaa")
"""
print("----------------1.基本数学计算--------------------")
print(eval("1+1"))

print("----------------2.字符串重复--------------------")
print(eval("'*'*50"))


print("----------------3.字符串转列表--------------------")
print(eval("[\"张三\",\"李四\",123]"))

print("----------------4.字符串转字典--------------------")
print(eval("{\"name\":\"张三\" ,\"age\":18 }"))
print(eval("{'name':'张三' ,'age':18 }"))  # 两种方式都一样

print("----------------5.直接转换input结果--------------------")
eval(input())  # __import__('os').system('touch aaa')
# eval("__import__('os').system('touch aaa')")
