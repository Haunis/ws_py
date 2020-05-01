"""
类方法和静态方法的区别:
    类方法持有类对象的引用可以访问类属性;
    静态方法一般不持有类引用,不需要访问类属性

"""


class Tool:
    count = 0  # 类属性

    @classmethod  # 定义类方法
    def print_count(cls):
        print("count = %d" % Tool.count)
        print("count = %d" % Tool.count)
        print("count = %d" % cls.count)  # 两种方式均可

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")

Tool.print_count()  # 调用类方法
