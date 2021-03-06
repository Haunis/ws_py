# -*-coding:utf-8-*-
"""
greenlet是基于yield的封装

安装greenlet:
    1.更新pip3: python3 -m pip install --upgrade pip
    2.官网下载适合python3版本的安装包 https://pypi.org/project/gevent/1.4.0/#files
    3.安装安装包: sudo pip3 install xxx.whl

或者直接sudo pip3 install greenlet

"""
from greenlet import greenlet
import time

g_count = 0;


def task_1():
    global g_count  # 使用global修饰可以访问并修改全局变量，否则只能当作局部变量修改
    while True:
        print("1")
        gr2.switch()  # 切换到gr2执行
        time.sleep(0.5)
        g_count += 1
        if g_count > 10:
            break


def task_2():
    global g_count
    while True:
        print("2")
        gr1.switch()
        time.sleep(0.5)
        g_count += 1
        if g_count > 10:
            break


gr1 = greenlet(task_1)
gr2 = greenlet(task_2)


def main():
    gr1.switch()  # 切换到gr1执行


if __name__ == "__main__":
    main()
