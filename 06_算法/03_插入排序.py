"""
将列表分为两部分，前面排好的是有序的，后面未排序的是无序
操作后面无序的第一个元素时，挨个和前面有序的元素从后向前比较

最坏时间复杂度：O(n^2)
最优时间复杂度:O(n)；如果列表本身是有序的，加入break判断进行优化后

稳定性： 稳定
"""


def sort(li):
    for i in range(1, len(li)):  # 假设li[0]是有序的，对后面的元素进行插入排序
        for j in range(i, 0, -1):  # 每次li[i]都当作前面有序元素的最后一个元素，并挨个和前面的元素进行比较
            if li[j] < li[j - 1]:  # 小于前面的元素则交换
                li[j], li[j - 1] = li[j - 1], li[j]
            else:  # 优化; 时间复杂度提升到O(n)
                break


def main():
    li = [3, 48, 2, 7, 1, 12, 37, 0, 4, 4, 11]
    print(li)
    sort(li)
    print(li)


if __name__ == "__main__":
    main()
