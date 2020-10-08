"""
二分查找也叫折半查找
二分查找的前提：
    1.序列必须是有序的
    2.这些元素必须相邻放置(就是说这个序列支持下标索引)。
    列表支持按位置定位元素满足这两个条件，链表不满足(不是很明白，链表也可以做到按位置索引）

最坏时间复杂度： O(log2(n)),一般写成O(logn)
最优时间复杂度： O(1)
"""


# 使用while查找
def binary_search1(li, element):
    first_index = 0
    last_index = len(li) - 1

    while first_index <= last_index:  # “=”可以比较首尾两个元素
        mid_index = (first_index + last_index) // 2
        if element < li[mid_index]:
            last_index = mid_index - 1
        elif element > li[mid_index]:
            first_index = mid_index + 1
        else:  # element和li[mid_index]正好相等
            return mid_index
    return -1  # 列表中无该元素


# 递归
def binary_search2(li, element, start_index, end_index):
    if start_index > end_index:
        return -1  # 列表中不包含该元素
    mid_index = (start_index + end_index) // 2
    if element < li[mid_index]:
        ret = binary_search2(li, element, start_index, mid_index - 1)
    elif element > li[mid_index]:
        ret = binary_search2(li, element, mid_index + 1, end_index)
    else:  # element和li[mid_index]正好相等
        ret = mid_index
    return ret


def main():
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10]

    element = 0
    index = binary_search1(li, element)
    print("%d 在列表中的索引是:%d" % (element, index))

    index = binary_search2(li, element, 0, len(li) - 1)
    print("%d 在列表中的索引是:%d" % (element, index))


if __name__ == "__main__":
    main()
