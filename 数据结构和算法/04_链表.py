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

    def add(self, item):  # 添加到尾部
        node = Node(item)
        if self.head is None:
            self.head = self.tail = self.current = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, item):
        to_delete_node = None  # 要删除的节点
        pre_node = None  # 要删除节点的前一个节点
        # 找到要删除的节点
        for temp_node in self:
            if temp_node.item == item:
                to_delete_node = temp_node

        if to_delete_node is None:
            print("LinkedList no item :", item)
        else:
            # 找到要删除节点的前一个节点，找到后，将其直接指向要删除节点的后一个节点
            for temp_node in self:
                if temp_node.next == to_delete_node:
                    pre_node = temp_node
            if pre_node is None:  # 要删除的是头节点
                self.head = to_delete_node.next
                self.current = self.head
            else:
                pre_node.next = to_delete_node.next

    def contains(self, item):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.item == item:
                return True
            temp_node = temp_node.next
        return False

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

    print("ll.is_empty():", ll.is_empty())
    print("ll.length():", ll.length())
    for temp in ll:
        print(temp)

    contain = 33
    print("contains(%d) = %s" % (contain, ll.contains(contain)))
    ll.delete(3)
    print("after delete......")
    print("ll.length():", ll.length())
    for temp in ll:
        print(temp)


if __name__ == "__main__":
    main()
