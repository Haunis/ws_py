"""
将元组或者字典传递给有多值参数的函数时需要用到拆包
元组拆包:*var_tuple
字典拆包:**var_dict

如果一个函数有多个返回值，使用多个变量接收也叫拆包

"""


def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    return 111, 222


gl_tuple = 1, 2, 3, 4  # 定义元组可以不用括号
gl_dict = {"name": "lee", "age": 17}
print(*gl_dict)  # name age ;只打印key
# print(**gl_dict)  # 报错

print("---------------------拆包前---------------------------")
fun(gl_tuple, gl_dict)  # 如果不拆包,这两个变量传递到函数时,函数会使用args接收当做一个元组处理

print("---------------------拆包后---------------------------")
a, b = fun(*gl_tuple, **gl_dict)  # a,b 接收叫拆包； *gl_tuple,**gl_dict也叫拆包; 多少个返回值就必须多少参数，否则会crash
# tuple_temp = fun(*gl_tuple, **gl_dict)  # 当然也可以用元组接收返回值
print("a = %d" % a)
print("b = %d" % b)
