# -*-coding:utf-8-*-
"""
安装gevent:
    1.更新pip3: python3 -m pip install --upgrade pip
    2.官网下载适合python3版本的安装包 https://pypi.org/project/gevent/1.4.0/#files
    3.安装安装包: sudo pip3 install xxx.whl
或者直接 sudo pip3 install gevent

简介:
gevent是基于greenlet的封装,greenlet是基于yield的封装,使用协程实现.
gevent是网络并发库

原理:
gevent遇到耗时任务就会切换,如join(),gevent.sleep(),socket的accept(),conect()等
但这些方法必须是gevent的方法,遇到系统的scocket.accept(),connect(),time.sleep()等不会切换
解决方法:1.import monkey 2.monkey.pacth_all()
原理: monkey重新打包代码,将系统的耗时任务切换成gevent的耗时任务

gevent意义:
利用耗时时间去执行任务,本质还是单线程

优化:
    当有多个函数需要调用时,使用如g1.join(), g2.join()比较繁琐
    可使用gevent.joinall([gevent.spawn(fun,arg)...])一次启动多个函数

"""
import gevent
import time


def test_fun1(n):
    for i in range(n):
        print(gevent.getcurrent(), i, "test_fun1")
        # time.sleep(0.5)
        gevent.sleep(0.5)


def test_fun2(n):
    for i in range(n):
        print(gevent.getcurrent(), i, "test_fun2")
        # time.sleep(0.5)
        gevent.sleep(0.5)


def test_fun3(n):
    for i in range(n):
        print(gevent.getcurrent(), i, "test_fun3")
        # time.sleep(0.5)
        gevent.sleep(0.5)


def main():
    g1 = gevent.spawn(test_fun1, 5)  # g1就是greenlet
    g2 = gevent.spawn(test_fun2, 5)
    g3 = gevent.spawn(test_fun3, 5)

    print(g1, g2, g3)  # 三个都是greenlet

    g1.join()  # 耗时;等待test_fun1,test_fun2,test_fun3执行完才会往下执行
    print("g1 join completed ...........")
    g2.join()
    print("g2 join completed ...........")
    g3.join()
    print("g3 join completed ...........")


if __name__ == "__main__":
    main()
