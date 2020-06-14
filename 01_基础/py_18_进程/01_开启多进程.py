#! /usr/bin/python3
"""
程序：是没有运行的储存在硬盘上的文件，运行起来就是进程
进程：操作系统分配资源的单位。进程可以调用cpu、内存、硬盘、网卡等资源
    进程也是实现多任务的一种方式

进程的状态：
        启动            调度          结束
    新建------→  就绪 ←-------→  运行 ------→  死亡
                    ↖        ↙
             满足条件  ↖    ↙ 等待条件
                    等待（阻塞）
"""
import multiprocessing
import time


def fun1():
    while True:
        print("1---------------------")
        time.sleep(1)


def fun2():
    while True:
        print("2---------------------")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=fun1)
    p2 = multiprocessing.Process(target=fun2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
