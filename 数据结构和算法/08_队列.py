"""
队列:
    就像排队一样;从一端添加,从另外一端获取(FIFO)
    在队尾添加,队头取

双端队列:
    头部和尾部都可以进行添加和取出元素;可以看做两个栈合在一块
"""


# 普通队列
class Queue(object):
    def __init__(self):
        self.__list = list()

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)


# 双端队列
class Deque(object):
    def __init__(self):
        self.__list = list()

    def add_front(self, item):
        self.__list.insert(0, item)

    def pop_front(self):
        return self.__list.pop(0)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


def main():
    print("-----------------普通队列-------------------")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print("-----------------双端队列-------------------")
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    print(deque.pop_front())
    print(deque.pop_front())


if __name__ == "__main__":
    main()
