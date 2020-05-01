"""
模块中可以定义变量，函数，类
"""

g_num = 100


def fun():
    print("fun executed")


class Dog(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("%s run" % self.name)
