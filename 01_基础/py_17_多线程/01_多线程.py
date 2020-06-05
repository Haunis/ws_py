#! /usr/bin/python3
"""
并行:真正多核cpu执行任务
并发:假的的多任务,单核cpu使用时间片轮转或优先级调度的方式执行(cpu核心数小于任务数)
电脑里基本都是并发

主线程结束后，进程并不会结束；主线程会等待子线程结束后才结束；
这跟c++不一样，默认情况下主线程结束了，进程也就结束了

"""
import time
import threading

g_loop_count = 0;


def sing():
    for i in range(5):
        print("----sing---")
        time.sleep(1)


def dance():
    for i in range(5):
        print("----dance---")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        global g_loop_count  # 告诉解释器此变量是全局变量不是局部变量;修改此值,会直接修改全局变量的值;否则此变量只是定义一个局部变量
        if g_loop_count <= 4:
            thread_list = threading.enumerate()
            print("线程总数： %d" % len(thread_list))
            time.sleep(3)
            g_loop_count += 1
        else:
            break;


if __name__ == "__main__":
    main()
