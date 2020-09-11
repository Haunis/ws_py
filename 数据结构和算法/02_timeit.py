"""
列表的四种扩容方式：
    1.li.append()
    2.li = li1+li2
    3.li = list(range(10000))
    3.li = [x for x in range(10000)]
"""
from timeit import Timer


def test1():
    li = []
    for i in range(10000):
        li.append(i)
    # print("test1:", li)


def test2():
    li = []
    for i in range(10000):
        li += [i]
    # print("test2:", li)


def test3():
    li = list(range(10000))
    # print("test3:", li)


def test4():
    li = [x for x in range(10000)]
    # print("test4:", li)


time1 = Timer("test1()", "from __main__ import test1")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second = time1.timeit(1000)  # 1000次,返回时间单位是秒
print("time1:", t_second)

time2 = Timer("test2()", "from __main__ import test2")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second2 = time2.timeit(1000)  # 1000次,返回时间单位是秒
print("time1:", t_second2)

time3 = Timer("test3()", "from __main__ import test3")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second3 = time3.timeit(1000)  # 1000次,返回时间单位是秒
print("time1:", t_second3)

time4 = Timer("test4()", "from __main__ import test4")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second4 = time4.timeit(1000)  # 1000次,返回时间单位是秒
print("time1:", t_second4)