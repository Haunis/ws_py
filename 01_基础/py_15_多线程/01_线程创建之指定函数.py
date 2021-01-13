#! /usr/bin/python3
"""
线程创建方式1： 给Thread()指定函数

并行:真正多核cpu执行任务
并发:假的的多任务,单核cpu使用时间片轮转或优先级调度的方式执行(cpu核心数小于任务数)
电脑里基本都是并发

主线程会等待子线程结束
这跟c++不一样，默认情况下主线程不会等待子线程结束

"""
import time
import threading

g_loop_count = 0;
g_num_list = [11, 22]


def sing():
    for i in range(5):
        print("----sing---")
        time.sleep(1)


# 函数可以接收参数
# 传的是啥，接收的就是啥，与c++不一样，c++是从void*转换成具体指针类型
def dance(num_list):
    num_list.append(33)  # 因为和g_num_list是同一个引用所以可以修改列表里的值
    print("dance :id(num_list)=%#x" % (id(num_list)))
    for i in range(5):
        print("----dance---, num_list=%s" % (num_list))
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)  # 只是创建一个普通的类
    t2 = threading.Thread(target=dance, args=(g_num_list,))  # 可以给函数传参，注意传的是元组
    t1.start()  # 创建并运行线程
    t2.start()
    while True:
        global g_loop_count  # 告诉解释器此变量是全局变量不是局部变量;修改此值,会直接修改全局变量的值;否则此变量只是定义一个局部变量
        if g_loop_count <= 3:
            thread_list = threading.enumerate()
            print("线程总数： %d" % len(thread_list))
            time.sleep(3)
            g_loop_count += 1
        else:
            break;
    print("main g_num_list = %s" % (g_num_list))  # 访问全局变量可以不加global修饰
    print("main :id(g_num_list)=%#x" % (id(g_num_list)))


if __name__ == "__main__":
    main()
