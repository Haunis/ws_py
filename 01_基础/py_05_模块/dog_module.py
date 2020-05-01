"""
模块中可以定义全局变量,函数,类

每个导入的文件没有缩进的代码都会被执行

__name__: python内置属性.
    如果是被其他文件导入的,则保存的是模块名
    如果是做主程序入口,则保存的是"__main__"

"""

# 1.定义全局变量

g_num = 99;


# 2.定义函数
# 九九乘法表
def multiple_table():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d * %d = %d \t" % (j, i, j * i), end="")  # end=""意思是不换行
            j += 1
        print("")
        i += 1


def say_hello():
    print("dog_module say_hello")


# 3.定义类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("%s run" % self.name)
