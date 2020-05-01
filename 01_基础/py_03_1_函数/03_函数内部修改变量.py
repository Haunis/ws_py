"""
在函数内部使用赋值语句不会影响函数外部变量的值
但对于可变变量,如果在函数内修改变量内部的值,函数执行完成后,函数外部的变量也会做同步修改

"""


def square(x):
    print("x1=%d,id(x)=%#x" % (x, id(x)))
    x = x * x  # 不会修改函数外部x的值;内部的x只会重新指向一个对象
    print("x2=%d,id(x)=%#x" % (x, id(x)))


x = 100
print("外部1:x=%d,id(x)=%#x" % (x, id(x)))
square(x)
print("x=%d,id(x)=%#x" % (x, id(x)))
