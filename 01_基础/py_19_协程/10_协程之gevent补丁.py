# -*-coding:utf-8-*-
"""
gevent使用demo

当有多个函数需要调用时,使用如g1.join(), g2.join()比较繁琐
可使用gevent.joinall([gevent.spawn(fun,arg)...])一次启动多个函数
"""
from gevent import monkey
import gevent
import time


def fun(arg):
    for i in range(3):
        print(arg)
        time.sleep(1)


def main():
    monkey.patch_all()  # 使用gevent中的耗时代替系统api的耗时,使得gevent切换有效

    gevent.joinall([  # 相当于g1.join(),g2.join()...
        gevent.spawn(fun, "s1"),
        gevent.spawn(fun, "s2"),
        gevent.spawn(fun, "s3"),
    ])


if __name__ == "__main__":
    main()
