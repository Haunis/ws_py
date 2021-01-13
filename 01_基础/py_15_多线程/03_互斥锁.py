# -*-coding:utf-8-*-
"""
g_mutex = threading.Lock()
上锁:g_mutex.acquire();
    如果之前未上锁则上锁成功,如果之前已上锁,则等待阻塞在此
释放锁:g_mutex.release();释放锁,其他线程可获取此锁
"""
import threading
import time

g_num = 0
g_mutex = mutex = threading.Lock()


def fun1(count):
    g_mutex.acquire()
    global g_num
    for i in range(count):
        # 也可在此上锁
        g_num += 1
    g_mutex.release()


def fun2(count):
    g_mutex.acquire()
    global g_num
    for i in range(count):
        g_num += 1
    g_mutex.release()


def main():
    t1 = threading.Thread(target=fun1, args=(1000000,))
    t2 = threading.Thread(target=fun1, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(1)
    print("g_num=%d" % (g_num))


if __name__ == "__main__":
    main()
