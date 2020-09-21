"""
自定义单链表
"""


class Tool:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None  # 迭代用

    def add(self, item):
        node = SingleNode(item)
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
            print("no :", item)
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
        for temp in self:
            if temp.item == item:
                return True
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


class SingleNode(object):
    def __init__(self):
        self.next = None
        pass

    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)


def main():
    tool = Tool()
    tool.add(1)
    tool.add(2)
    tool.add(3)
    tool.add(4)
    for temp in tool:
        print(temp)

    # print(tool.contains(14))
    tool.delete(5)
    print("after delete......")
    for temp in tool:
        print(temp)


if __name__ == "__main__":
    main()
