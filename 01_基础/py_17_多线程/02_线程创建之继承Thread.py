#! /usr/bin/python3

"""
多线程创建方式2：通过继承Thread类的方法实现多线程

调用start()方法之后,线程启动时会自动调用Thread的run()方法


使用场景:线程做的事情比较复杂,在类里封装在各个函数做

"""

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("%d %s" % (i, self))
            time.sleep(1)


def main():
    t = MyThread()
    t.start()  # 调用start()会自动调用Mythread的run方法


if __name__ == "__main__":
    main()
