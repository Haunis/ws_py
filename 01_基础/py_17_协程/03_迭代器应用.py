# -*-coding:utf-8-*-
"""
使用迭代器生成 斐波那契数列
斐波那契数列: 0 1 1 2 3 5 8 13 ...

迭代器优点:节省内存空间.迭代器返回的是生成数据的方式,而不像列表占用大量内存

list(),tuple()等转换原理:
    以fibo_list = list(Fibonacci(10))为例
    1.生成一个空列表
    2.调用Fibonacci迭代方法向生成的空列表中添加元素
"""


class Fibonacci(object):
    def __init__(self, total_num):
        self.total_num = total_num
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.total_num:
            ret = self.a
            # temp = self.a
            # self.a = self.b
            # self.b = temp + self.b
            (self.a, self.b) = (self.b, self.a + self.b)
            self.count += 1
            return ret
        else:
            raise StopIteration


def main():
    for num in Fibonacci(10):
        print(num)
    fibo_list = list(Fibonacci(10))
    print(fibo_list)


if __name__ == "__main__":
    main()
