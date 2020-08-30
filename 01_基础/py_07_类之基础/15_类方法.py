"""
类方法和静态方法的区别:
    类方法持有类对象的引用可以访问类属性;
    静态方法一般不持有类引用,不需要访问类属性
类方法和实例方法的区别：
    调用类方法传类对象的引用给方法，调用实例方法传实例对象的引用给方法


类方法就是用来修改类属性的

也可以通过实例对象的__class__属性对类属性进行修改
__class__属性：该属性指向类对象


"""


class Tool:
    count = 0  # 类属性

    @classmethod  # 语法糖，定义类方法
    def print_count(cls):  # cls指向类对象,是形参可以任意指定名称
        print("count = %d" % Tool.count)
        print("count = %d" % cls.count)  # 两种方式均可

    def __init__(self, name):  # self指向实例对象
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")

Tool.print_count()  # 调用类方法
