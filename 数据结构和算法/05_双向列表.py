"""
自定义双向链表
"""


class DoubleLink(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def delete(self, item):
        cur = self.head
        if cur is None:
            print("空链表,无需删除")
            return
        if cur.item == item:
            self.head = self.head.next
            self.head.pre = None
            return
        while cur is not None:
            if cur.item == item:
                cur.pre.next = cur.next
                cur.next.pre = cur.pre  # 双向删除
                return
            cur = cur.next
        print("删除失败，无此元素 :", item)

    def contains(self, item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def insert(self, pos, item):
        node = Node(item)
        cur = self.head
        if pos == 0:
            if cur is None:
                self.head = node
            else:
                node.next = self.head
                self.head.pre = node
                self.head = node
        else:
            count = 0
            while cur is not None:
                if count == pos:
                    cur.pre.next = node
                    node.pre = cur.pre
                    node.next = cur
                    cur.pre = node
                    return
                cur = cur.next
                count += 1
            print("超出链表长度范围")

    def insert_head(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.item, end="\t")
            cur = cur.next
        print()

    def is_empty(self):
        return self.head is None


class Node(object):
    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


def main():
    ll = DoubleLink()
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
    ll.insert(3, -22)
    ll.traverse()


if __name__ == "__main__":
    main()
