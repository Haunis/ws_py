"""
二叉树性质:
    1.在二叉树的第n层上,最多只有2^(n-1)个节点
    2.深度为k的二叉树最多有2^k-1个节点;  s = 1*(1-2^k)/(1-2)=2^k-1
    3.对于任意二叉树,如果叶节点为N0,而度数为2的节点总数为N2,则N0=N2+1
    4.具有n个节点的完全二叉树,其深度必为log2(n+1)
    5.对于完全二叉树,若从上至下,从左至右进行编号,则编号为i的节点,其左孩子的编号必为2i,
        右孩子的编号必为2i+1;其双亲编号必为i/2(i=1时为根,除外)

广度优先遍历:
    向完全二叉树中添加元素,按从上往下从左网友的顺序添加,遍历时也采用该顺序
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, item):  # 采用广度优先的遍历方式,遍历每一层,向度不为2的节点添加节点
        node = Node(item)
        leaf_node = self.__find_node()
        if leaf_node is None:
            self.root = node
        elif leaf_node.l_child is None:
            leaf_node.l_child = node
        elif leaf_node.r_child is None:
            leaf_node.r_child = node
        self.count += 1

    def add2(self, item):  # 也是广度优先,思路有所改变
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        li = [self.root]
        while li is not None:  # 只要队列不为空,就一直往后找
            cur_node = li.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                li.append(cur_node.l_child)
            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                li.append(cur_node.r_child)

    def __find_node(self):  # 找到度不为2的节点
        if self.root is None:
            return None
        li = list()
        li.append(self.root)
        head = li[0]
        while head.l_child is not None and head.r_child is not None:
            li.append(head.l_child)
            li.append(head.r_child)
            li.pop(0)
            head = li[0]
        return head

    def breadth_traverse(self):  # 广度优先遍历
        if self.root is None:
            print("empty")
            return
        li = list()
        li.append(self.root)
        index = 0
        head = li[index]
        while head.l_child is not None or head.r_child is not None:
            li.append(head.l_child)
            if head.r_child is not None:
                li.append(head.r_child)
            index += 1
            head = li[index]
        for node in li:
            print(node.item)
        print("size:", len(li))


def main():
    tree = Tree()
    for i in range(1, 100):
        tree.add2(i)
    tree.breadth_traverse()


if __name__ == "__main__":
    main()
