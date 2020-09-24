"""
自定义单链表
"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None  # 迭代用

    def is_empty(self):
        return self.head is None

    def length(self):
        tempNode = self.head
        count = 0
        while tempNode is not None:
            tempNode = tempNode.next
            count += 1
        return count

    def insert_head(self, item):  # 添加到头部,头插法
        node = Node(item)
        node.next = self.head
        self.head = node

    def insert(self, pos, item):
        node = Node(item)
        if pos >= self.length():
            print("越界")
        else:
            if pos == 0:
                node.next = self.head.next
                self.head = node
            else:
                count = 0
                pre_node = self.head
                while count < pos - 1:
                    pre_node = pre_node.next
                    count += 1
                node.next = pre_node.next
                pre_node.next = node

    def add(self, item):  # 添加到尾部;尾插法
        node = Node(item)
        if self.head is None:
            self.head = self.tail = self.current = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, item):
        if self.contains(item):
            if self.head.item == item:
                self.head = self.head.next
            else:
                pre_node = self.head  # 要删除节点的前一个节点
                while pre_node.next.item != item:
                    pre_node = pre_node.next
                pre_node.next = pre_node.next.next
        else:
            print("不包含该节点!!!!")

    def contains(self, item):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.item == item:
                return True
            temp_node = temp_node.next
        return False

    def traverse(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.item, end="\t")
            cur_node = cur_node.next
        print()

    def __iter__(self):  # 可迭代对象
        return self

    def __next__(self):  # 实现 __iter__和__next__是迭代器
        if self.current is not None:
            temp = self.current
            self.current = self.current.next
            return temp
        else:
            self.current = self.head
            raise StopIteration


class Node(object):
    def __init__(self):
        self.next = None
        pass

    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)


def main():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)

    ll.traverse()
    print("ll.is_empty():", ll.is_empty())
    print("ll.length():", ll.length())

    print("contains(33):", ll.contains(33))

    print("\n---------------delete 3 -----------------------")
    ll.delete(1)
    ll.traverse()

    print("\n----------------insert_head(-11)-----------------")
    ll.insert_head(-11)
    ll.traverse()

    print("\n----------------insert(2,-22)-----------------")
    ll.insert(2, -22)
    ll.traverse()


if __name__ == "__main__":
    main()
