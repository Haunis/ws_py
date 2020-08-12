"""
将元组或者字典传递给有多值参数的函数时需要用到拆包
元组拆包:*var_tuple
字典拆包:**var_dict

如果一个函数有多个返回值，使用多个变量接收也叫拆包

对于定义的fun(*args,**kwargs):
    *args--代表接收不定长参数
    args--元组
    **kwargs--代表接收不定长的带名字的参数
    kwargs--字典

对于调用fun(*args,**kwargs):
    *args -- 代表对元组args进行拆包
    args--元组
    **kwargs--代表对字典进行拆包
    kwargs--字典
"""


def fun(*args, **kwargs):
    print("fun args:", args)  # args是元组
    print("fun kwargs:", kwargs)  # kwargs是字典
    fun2(*args, **kwargs)  # 对元组和字典进行拆包传递


def fun2(*args, **kwargs):
    print("--------------")
    print("fun2 args:", args)  # args是元组
    print("fun2 kwargs:", kwargs)  # kwargs是字典


gl_tuple = 1, 2, 3, 4  # 定义元组可以不用括号
gl_dict = {"name": "lee", "age": 17}
print("*gl_dict:", *gl_dict)  # name age ;只打印key
# print(**gl_dict)  # 报错
print("*gl_tuple:", *gl_tuple)
# print("type(*gl_tuple):", type(*gl_tuple))报错

print("---------------------直接传参数---------------------------")
fun(11, 22, name="hh", age=12)

print("---------------------拆包前---------------------------")
fun(gl_tuple, gl_dict)  # 如果不拆包,这两个变量传递到函数时,函数会使用args接收当做一个元组处理

print("---------------------拆包后调用---------------------------")
# a,b 接收叫拆包； *gl_tuple, **gl_dict也叫拆包; 多少个返回值就必须多少参数，否则会crash
# 就相当于调用fun(1,2,3,4,name="lee",age=17)
fun(*gl_tuple, **gl_dict)
