"""
函数需要接收多个参数时:
    *args,可以接收元组
    **kwargs,可以接收字典
格式: fun(*args,**kwargs)
"""


def fun(num, *args, **kwargs):
    print(num)  # 1
    print(args)  # 2 3 4
    print(kwargs)  # {'name': 'lee', 'age': 12}


fun(1, 2, 3, 4, name="lee", age=12)
