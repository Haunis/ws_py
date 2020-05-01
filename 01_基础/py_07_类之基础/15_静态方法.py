#! /usr/bin/python3

"""
静态方法：既不需要访问类属性也不需要访问实例属性
		方法不需要传参；在方法上面用 @staticmethod修饰即可
"""


class Dog(object):
    @staticmethod
    def run():
        print("Dog run")


Dog.run()
