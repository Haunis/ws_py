#! /usr/bin/python3

"""
静态方法：既不需要访问类属性也不需要访问实例属性
		方法不需要传参；在方法上面用 @staticmethod修饰即可
为何需要静态方法?
    有些方法是类和实例公用,但又不想别的类使用
调用静态方法:
    1.在类里的方法调用:self.staticFun()
    2.在类外部调用:类名.staticFun()
"""


class Dog(object):
    @staticmethod
    def run():
        print("Dog run")

    def test(self):
        self.run()


Dog.run()
Dog().test()
