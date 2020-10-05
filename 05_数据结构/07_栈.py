"""
栈和线性表的区别:
    顺序表和链表解决的是数据怎么存放的问题
    栈是描述的是支持何种操作(LIFO),其实现可以是顺序表也可以是链表

栈:
    存储的是线性表(顺序表,链表),是一个容器
    不用关心其物理上是怎么存储的,关心的是其支持什么操作

特点:只有一个口,就像一个杯子,后进先出(LIFO,last in first out )

可以用顺序表实现,也可以用链表实现,本示例使用list实现(python中的list就是顺序表)
"""


class Stack(object):
    def __init__(self):
        self.__list = list()

    def push(self, item):  # 压栈,向栈顶添加元素
        self.__list.append(item)

    def pop(self):  # 出栈,取出栈顶元素
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

    def peek(self):  # 返回栈顶元素
        return self.__list[-1]


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
