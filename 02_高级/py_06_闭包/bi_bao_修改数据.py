"""
闭包里的变量都是局部变量
创建的每两个闭包之间都是互不相干的,都不会能访问彼此变量的值
"""


def outter():
    x = 100

    def inner():
        nonlocal x
        print("before x = %s" % x)
        x = 200  # 会直接修改x的值,nonlocal和global作用相似
        print("after x = %s" % x)

    return inner


print("---------fun1---------")
fun1 = outter()
fun1()

fun1()  # 这次使用闭包里数据已经被修改

print("\n---------fun2---------")
fun2 = outter()  # 返回的新函数,刚开始时x还是等于100
fun2()
