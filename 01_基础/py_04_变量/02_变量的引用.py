"""
变量和数据是分开保存的
变量中记录数据内存的地址，叫做引用

如果一个变量已经被定义，再给这个变量赋值的时候，本质上修改了变量的引用
1.变量不再对之前的数据引用
2.变量改为对新数据的引用
（跟java中常量池相似，跟c/c++不同，c/c++，每次变量赋新值都会创建新的数据）

调用函数传递的是实参的引用, 调用的函数用一个变量接收实参的引用(指向同一个对象实体,id()获取的是对象实体的地址,所以会相等)
返回的也是数据的引用,而不是数据本身
是值传递,只不过传递的是引用,和java一样??
"""


def test(num):
    # num是个新变量,和java类似,和调用出处变量指向同一个引用
    print("id(num):%#x" % id(num))  # 地址和调用的地方a的地址相等
    num = 1000
    print("id(num):%#x" % id(num))  # 会改变
    str = "hello"
    print("id(str):%#x" % id(str))
    return str  # 返回str的引用


a = 12
b = a
print("id(a):%#x" % id(a))
print("id(b):%#x" % id(b))  # 两者想等,c/c++中不等
result = test(a)
print("result=%s, id(result)=%#x" % (result, id(result)))
