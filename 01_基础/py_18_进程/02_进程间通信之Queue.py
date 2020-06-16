# -*-coding:utf-8-*-
"""
进程间通信方式:
    1.socket
    2.文件 (效率低)
    3.队列,特点:先进先出,是内存里的一块内存空间

Queue:
    创建好队列之后,队列里可以放任意数据
    只能用在同一个程序里的多个进程,而且是同一台电脑
"""
import multiprocessing


def put_msg(queue):
    temp_list = [11, 22, 33]
    for data in temp_list:
        queue.put(data)
    print("put_msg execute: %s" % str(temp_list))


def get_msg(queue):
    # temp_list = []
    temp_list = list()
    while True:
        data = queue.get()
        temp_list.append(data)
        if queue.empty():
            break
    print("get_msg : %s" % str(temp_list))


def main():
    # queue = multiprocessing.Queue(3)
    queue = multiprocessing.Queue()  # 不传参的话默认容量是最大
    p1 = multiprocessing.Process(target=put_msg, args=(queue,))
    p2 = multiprocessing.Process(target=get_msg, args=(queue,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
