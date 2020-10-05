"""
将列表分两部分，左边有序，右边无序，就是从右边无须的找到最小的放到左边来

思路0：
    假设前面的元素是有序的，现在要将第i个元素插入到正确位置
    从前面有的元素第0个开始，和第i元素进行比较，比第i个元素大则交换
    该方法交换元素太频繁。。。

思路1：
    假设索引0位置的值最小,其后面的元素挨个和该元素进行比较,如果比该元素小则交换
    一轮比较下来后,索引0位置的元素就最小
    再假设索引1位置的元素值最小...

思路2：
    思路1有个缺陷：如果后面的值比假设的值小，每次都要交换两个位置的值
    改进： 用一个值记录最小值的索引,如果索引有变再交换两个位置的值

时间复杂度O(n^2)
即使是个有序的还是O(n^2),无法优化

稳定性：不稳定
    如果排序按选最小值在最前的进行升序排列，就稳定
    但是按选最大值在最后的升序进行排列，不稳定
"""


# 太绕了，忘了该方法吧。。。
def sort0(li):
    for i in range(1, len(li)):
        for j in range(i):
            if li[j] > li[i]:  # 每次将前面有序的的元素和li[i]进行比较
                li[i], li[j] = li[j], li[i]


# 比假设位置处的值小，则交换两位置的值
def sort1(li):
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]


####### 这个是真正的选择排序#######
def sort2(li):
    for i in range(len(li)):
        min_index = i  # 用一个变量记录最小位置的索引
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]


def main():
    li = [3, 48, 2, 7, 1, 12, 37, 0, 4, 11]
    print(li)
    # sort1(li)
    sort2(li)
    print(li)


if __name__ == "__main__":
    main()
