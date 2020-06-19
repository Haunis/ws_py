#! /usr/bin/python3
"""
判断某个数据类型a是否可以迭代： isinstance(stu,Iterable)
自定义对象可迭代的条件:
    1.实现__iter__(self)方法,实现该方法后isinstance(stu,Iterable)就返回true
    2.__iter__(self)返回自定义迭代器 MyIterator
    3.自定义迭代器(MyIterator): 实现__iter__(self)和__next__(self)方法的对象就是迭代器

for循遍历某个对象(stu)流程:
1.判断是否是可迭代对象: isinstance(stu,Iterable)
2.调用iter(stu)函数,此函数会自动调用stu.__iter__(self)得到迭代器MyIterator
3.调用next(myIteraton)函数,此函数会自动调用迭代器myIterator的__next__(self)方法,得到返回值
for循环每走一次都会调用迭代器的__next__(self)方法

"""
from collections import Iterable
import time


class Student(object):
    def __init__(self):
        self.name_list = list()

    def add(self, name):
        self.name_list.append(name)

    def __iter__(self):  # 实现该方法后,isinstance(stu,Iterable)返回True
        return MyIterator(self)


class MyIterator(object):
    def __init__(self, stu):
        self.stu = stu

    def __iter__(self):
        pass

    def __next__(self):
        return 11


def main():
    stu = Student()
    is_iterable = isinstance(stu, Iterable)  # 是否是Iterable的实例(子类也行)
    print("is_iterable = %s" % is_iterable)

    stu.add("张三")
    stu.add("李四")
    stu.add("王五")

    for temp in stu:
        print(temp)
        time.sleep(1)


if __name__ == "__main__":
    main()
