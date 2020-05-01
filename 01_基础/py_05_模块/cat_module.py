"""
模块中可以定义全局变量,函数,类

每个导入的文件没有缩进的代码都会被执行

__name__: python内置属性.
    如果是被其他文件导入的,则保存的是模块名
    如果是做主程序入口,则保存的是"__main__"
"""


def main():
    print("main executed")


# 如果该文件作为主程序入口则执行main(),否则该文件只是被当做一个模块
if __name__ == "__main__":
    main()
print("cat_module called ,__name__ = %s" % __name__)  # 模块的测试函数放到main()里,尽量不要放到外面

g_cat_age = 3


class Cat:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("%s run" % self.name)


def say_hello():
    print("cat_module say_hello")
