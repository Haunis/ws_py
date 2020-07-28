#! /usr/bin/python3

"""
由于c语言写的解释器有GIL锁的存在，导致同一时刻只能有一个线程在运行
不能发挥cpu多核的优势，最后看到的效果就是占两个cpu核，但每个核只利用了50%

用java写的解释器没有该问题
"""
import threading

def dead_loop():
    while True:
        pass

def main():
    t = threading.Thread(target=dead_loop)
    t.start()

    while True:
        pass

if __name__ == "__main__":
    main()
