# -*-coding:utf-8-*-
"""
通过进程池创建的子进程,主进程不会等待其结束才结束

"""
from multiprocessing import Pool
import os, random, time


def work(msg):
    time_start = time.time()
    print("%s 开始执行 pid=%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)  # random.random() 0~1
    time_end = time.time()
    print("%s 执行完毕 耗时=%.2f" % (msg, time_end - time_start))


def main():
    pool = Pool(3)  # 进程池中缓存3个进程
    for i in range(10):
        msg = "msg" + str(i)
        pool.apply_async(work, (msg,))

    print("-------start-------")
    pool.close()  # 关闭进程池,关闭后,pool不再接收新的请求
    pool.join()  # 调用的进程会等待pool中所有子进程执行完成(调用处被阻塞),必须在close()之后
    print("-------end-------")


if __name__ == "__main__":
    main()
