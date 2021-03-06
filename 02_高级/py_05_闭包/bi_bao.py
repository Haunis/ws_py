"""
闭包：就是在函数里定义函数，内部函数用到了外部函数里的变量,外部函数返回内部定义的函数的引用
    这两层函数在一块称为闭包

将内部函数以及内部函数用到的变量(如本例中的k,b,x)，这两部分称为闭包

闭包和普通函数区别:
    拿到普通函数的引用后,只能使用函数里的代码功能
    但是拿到闭包的引用后,不仅能使用函数里的代码功能,且该函数还可以使用闭包的数据

普通函数:封装代码,拿到引用后可以使用其功能(代码执行逻辑)
匿名函数:也是函数,可以封装一部分代码,简单;可以当实参;拿到引用后可以使用其功能
闭包:比函数高端,不仅可以封装代码,而且可以使用指定的变量;拿到引用后不仅可以使用其功能,还可以使用其数据
对象:功能比闭包更复杂;拿到引用后可以使用其功能和数据

与其使用闭包为何不使用全局变量?
    全局变量不安全
使用闭包为何不使用对象?
    对象比闭包占用内存空间更多

"""


def line(k, b):
    def create_y(x):  # 定义函数
        print(k * x + b)  # 使用指定的变量

    return create_y  # 返回函数的引用


fun = line(1, 2)
print(type(fun))
fun(3)
