#! /usr/bin/python3

"""
解决GIL：
    1.换非cpython解释器，如java写的解释器
    2.多线程使用别的语言，如c语言
"""

from ctypes import *
from threading import Thread


def main():
    lib = cdll.LoadLibrary("./libdead.so")  # 加载动态链接库
    t = Thread(target=lib.deadLoop)
    t.start()
    while True:
        pass  # 占位符


if __name__ == "__main__":
    main()
