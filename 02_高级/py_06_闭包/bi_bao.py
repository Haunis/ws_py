"""
闭包：就是在函数里定义函数，并返回内部定义的函数的引用

将内部函数以及内部函数用到的变量(如本例中的k,b,x)，这两部分称为闭包
"""


def line(k, b):
    def create_y(x):  # 创建不同缺省值的函数
        print(k * x + b)

    return create_y  # 返回函数的引用


fun = line(1, 2)
print(type(fun))
fun(3)
