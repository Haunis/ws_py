# -*-coding:utf-8-*-
"""
将可迭代对象和迭代器合二为一(就是完善迭代器方法即可)
可迭代对象:实现__iter__(self)方法的对象
迭代器:实现__iter__(self)和__next__(self)方法的对象

迭代器优点:节省内存空间;保存的是生成数据的方式,而不是生成数据的结果

例子:python2.x中 range(10)直接返回一个列表,xrange()返回生成数据的方式(类)
    所以xrange()比range()更节省内存空间
python3.x已优化range(),range(10)返回的也是一个对象

"""


class Student:
    def __init__(self):
        self.name_list = list()
        self.currentNum = 0

    def add(self, name):
        self.name_list.append(name)

    def __iter__(self):  # 有了此方法便是可迭代对象
        return self  # 返回迭代器

    def __next__(self):
        if self.currentNum < len(self.name_list):
            ret = self.name_list[self.currentNum]
            self.currentNum += 1
            return ret
        else:
            raise StopIteration


def main():
    stu = Student()
    stu.add("张三")
    stu.add("李四")
    stu.add("王五")
    stu.add("赵六")
    for name in stu:
        print(name)


if __name__ == "__main__":
    main()
