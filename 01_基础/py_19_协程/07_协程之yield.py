"""
使用协程完成多任务
利用yield的特性，使得多个任务在一个线程里实现调度

进程占用资源最多，多线程次之，协程占用资源最少
协程:假并发,是一个进程里的一个线程的任务.无非是yield让任务暂停,切换到另一处执行

使用封装好的greenlet也可完成多任务,greenlet也是基于yield
gevent是封装的greenlet
"""
import time


def task_1():
    while True:
        print("1")
        time.sleep(0.5)
        yield


def task_2():
    while True:
        print("2")
        time.sleep(0.5)
        yield


# task_1和task_2交替执行,完成并发任务
def main():
    t1 = task_1()  # 得到生成器
    t2 = task_2()
    while True:
        next(t1)  # 执行task_1,并暂停在yield,等待下一次next(t1)
        next(t2)


if __name__ == "__main__":
    main()
