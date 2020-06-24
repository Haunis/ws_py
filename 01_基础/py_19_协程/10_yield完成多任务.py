"""
进程占用资源最多，多线程次之，协程占用资源最少

"""
import time


def task_1():
    while True:
        print("1")
        time.sleep(0.5)
        yield


def task_2():
    while True:
        print("2")
        time.sleep(0.5)
        yield


def main():
    t1 = task_1()  # 得到生成器
    t2 = task_2()
    while True:
        next(t1)  # task_1和task_2交替执行,完成并发任务
        next(t2)


if __name__ == "__main__":
    main()
