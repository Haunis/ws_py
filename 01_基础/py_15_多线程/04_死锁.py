# -*-coding:utf-8-*-
"""
如何避免死锁:
    1.添加超时时间
    2.程序设计时避免:银行家算法--安排好流程,哪个锁先解,哪个锁后解
"""
import threading
import time

g_mutex1 = threading.Lock()
g_mutex2 = threading.Lock()


def fun1():
    print("fun1 called")
    g_mutex1.acquire()
    time.sleep(1)
    print("fun1 g_mutex2 acquiring...")
    g_mutex2.acquire()
    print("fun1 success")
    g_mutex2.release()
    g_mutex1.release()


def fun2():
    print("fun2 called")
    g_mutex2.acquire()
    time.sleep(1)
    print("fun1 g_mutex1 acquiring...")
    g_mutex1.acquire()
    print("fun2 success")
    g_mutex1.release()
    g_mutex2.release()


def main():
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
