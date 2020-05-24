#! /usr/bin/python3

"""
函数返回多个值时，可以包装成一个元组返回
如果是直接返回的话，可以省略小括号

可以用多个变量接收函数返回的元组，变量的个数应该和元组内元素个数相等

函数接收和返回的都是引用


"""


def measure():
    print("*****measure()开始**********")
    height = 80
    width = 100
    print("id(height):%#x" % id(height))
    print("id(width):%#x" % id(width))

    temp_tuple = (height, width)
    print("id(temp_tuple):%#x" % id(temp_tuple))
    # return (height,width)
    # return height,width #如果直接返回元组可以省略小括号
    print("*****measure()结束**********")
    return temp_tuple  # 返回temp_tuple,height,widht的引用


print("\n\n-----------------1.元组接收返回值--------------------")
result_tuple = measure()
print("id(result_tuple):%#x" % id(result_tuple))  # 和函数里的元组地址相等
print("type(result_tuple):%s" % type(result_tuple))
print("id(result_tuple[0]):%#x" % id(result_tuple[0]))
print("id(result_tuple[1]):%#x" % id(result_tuple[1]))
print("result_tuple:", result_tuple)

print("\n\n--------------2.两个变量接收返回值--------------------")
gl_height, gl_width = measure()  # 拆包
print("id(gl_height):%#x" % id(gl_height))
print("id(gl_width):%#x" % id(gl_width))
print("gl_height:%d, gl_width:%d" % (gl_height, gl_width))

print("\n\n--------------3.交换变量--------------------")
a = 2
b = 100
print("交换前：a=%d,b=%d" % (a, b))
a = a + b
b = a - b
a = a - b
print("交换后：a=%d,b=%d" % (a, b))

# 使用python特有的方式进行交换
a = 2
b = 100
print("交换前：a=%d,b=%d" % (a, b))
# a,b = (b,a)
a, b = b, a  # 可以省略小括号
print("交换后：a=%d,b=%d" % (a, b))
