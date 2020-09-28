"""
自定义单向循环链表
所谓单向循环链表是指尾节点指向头结点
"""


class CircleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur_node = self.head
        if cur_node is None:
            count = 0
        else:
            count = 0
            while cur_node.next is not self.head:
                cur_node = cur_node.next
                count += 1
            count += 1  # 算上尾节点
        return count

    def insert_head(self, item):  # 添加到头部,头插法
        node = Node(item)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            tail_node = self.head
            while tail_node.next is not self.head:
                tail_node = tail_node.next
            tail_node.next = node
            node.next = self.head
            self.head = node

    def insert(self, pos, item):
        node = Node(item)
        if pos > self.length():
            print("越界")
        elif pos == self.length():
            self.add(item)
        else:
            if pos == 0:
                self.insert_head(node)
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
            self.head = node
            node.next = node
        else:
            tail_node = self.head
            while tail_node.next is not self.head:
                tail_node = tail_node.next
            tail_node.next = node
            node.next = self.head

    def delete(self, item):
        if self.contains(item):
            if self.head.item == item:
                tail_node = self.head
                while tail_node.next is not self.head:  # 找出尾节点
                    tail_node = tail_node.next
                if tail_node is self.head:  # 链表中就一个节点
                    self.head = None
                else:
                    tail_node.next = self.head.next
                    self.head = tail_node.next
            else:
                pre_node = self.head  # 要删除节点的前一个节点
                while pre_node.next.item != item:
                    pre_node = pre_node.next
                pre_node.next = pre_node.next.next
        else:
            print("不包含该节点!!!!")

    def contains(self, item):
        cur_node = self.head
        if cur_node is None:
            return False
        elif cur_node.next is self.head:
            return self.head.item == item
        else:
            while cur_node.next is not self.head:
                if cur_node.item == item:
                    return True
                cur_node = cur_node.next
            return False

    def traverse(self):
        cur_node = self.head
        if cur_node is None:
            print("traverse:空列表")
        else:
            while cur_node.next is not self.head:
                print(cur_node.item, end="\t")
                cur_node = cur_node.next
            print(cur_node.item)  # 打印尾节点


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
    ll = CircleLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)

    ll.traverse()
    print("ll.is_empty():", ll.is_empty())
    print("ll.length():", ll.length())

    print("contains(33):", ll.contains(33))

    print("\n---------------delete 3 -----------------------")
    ll.delete(3)
    ll.traverse()

    print("\n----------------insert_head(-11)-----------------")
    ll.insert_head(-11)
    ll.traverse()

    print("\n----------------insert(2,-22)-----------------")
    ll.insert(2, -22)
    ll.traverse()


if __name__ == "__main__":
    main()
