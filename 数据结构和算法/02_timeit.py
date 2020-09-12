"""
class timeit.Timer(stmt='pass',setup='pass',timer=<timer function>)
    第一个参数：要测试的代码语句(statment)
    第二个参数：运行时的依赖环境(导包)
    第三个参数：定时器函数，与平台有关

列表的几种扩容方式：
    1.li.append()
    2.li = li1+li2
    3.li = list(range(10000))
    4.li = [x for x in range(10000)]
    5.li.extend([i])
"""
from timeit import Timer


def test1():
    li = []
    for i in range(10000):
        li.append(i)
    # print("test1:", li)


def test2():  # 列表相加
    li = []
    for i in range(10000):
        li += [i]
    # print("test2:", li)


def test3():
    li = list(range(10000))
    # print("test3:", li)


def test4():  # 列表推导式
    li = [x for x in range(10000)]
    # print("test4:", li)


def test5():  # extend
    li = []
    for i in range(10000):
        li.extend([i])
    # print(li)


def test6():  # insert
    li = []
    for i in range(10000):
        li.insert(0, i)
    # print(li)


time1 = Timer("test1()", "from __main__ import test1")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second = time1.timeit(1000)  # 1000次,返回时间单位是秒
print("time1 append:", t_second)

time2 = Timer("test2()", "from __main__ import test2")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second2 = time2.timeit(1000)  # 1000次,返回时间单位是秒
print("time2 +:", t_second2)

time3 = Timer("test3()", "from __main__ import test3")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second3 = time3.timeit(1000)  # 1000次,返回时间单位是秒
print("time3 list(range()):", t_second3)

time4 = Timer("test4()", "from __main__ import test4")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second4 = time4.timeit(1000)  # 1000次,返回时间单位是秒
print("time4 推导式:", t_second4)

time5 = Timer("test5()", "from __main__ import test5")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second5 = time5.timeit(1000)  # 1000次,返回时间单位是秒
print("time5 extend:", t_second5)

time6 = Timer("test6()", "from __main__ import test6")  # 第一个参数并是在当前文件执行;如果当前文件是启动文件，名字就是__main__
t_second6 = time6.timeit(1000)  # 1000次,返回时间单位是秒
print("time6 insert:", t_second6)
