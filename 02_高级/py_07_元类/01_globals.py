"""
globals()返回一个字典,里面保存所有全局变量
包括 builtin内置模块

调用print()函数的调用链:
    globals()找有没这个函数 --> 到globals()里的__builtins__指向的模块里找
"""
aaa = 3


def bbb():
    print("bbb called")


class ccc(object):
    def __init__(self):
        print("class ccc called")


instance_c = ccc()
ret = globals()
print(ret)

mo = ret["__builtins__"]  # 返回builtin模块
mo.print("hhhh")  # 调用模块里的print函数
