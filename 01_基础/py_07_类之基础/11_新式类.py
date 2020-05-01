#! /usr/bin/python3
"""
新式类：以object为基类的类
旧式类：也叫经典类，不以object作为基类;不推荐使用

python2.x中，如果没有指定父类则不会以object作为基类，是旧式类
python3.x中，都是新式类

python2.x中定义新式类：class Demo(object):

新式类和旧式类在多继承时，会影响到方法的搜索顺序

为了保证代码可以运行在python2.x和python3.x建议所有的类都定义成新式类
"""


class Demo(object):  # 没有指定父类的类,定义时都建议其父类为object;以便其在python2.x也能正常运行
    pass


demo = Demo()

print(dir(demo))
