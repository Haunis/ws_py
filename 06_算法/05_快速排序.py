"""
>>>>>>>>>>>>>>必须要掌握<<<<<<<<<<<<<<<
快速排序：
    就是将序列的第一个元素放入正确的位置--该位置前面的元素都比该元素小，后面的元素都比该元素大,该位置也是最终该元素在序列的位置

实现思路:
    设一个low游标和一个high游标
    1.low游标从第二个元素开始往后走，遇到比第一个元素大的停下来
    2.high游标从最后向前走，遇到比第一个元素小的停下来
    3.这时交换low和high位置的元素，然后继续移动游标，直至low和high游标重合
    4.这个时候将第一个元素插入到low和high重合索引的前面，比如该位置索引为x
    5.以该索引x为界，将序列分成两个部分，前面的都比x处值小，后面的都比x处值大。继续对两个子序列重复1 2 3 4 步骤

本例代码实现和上述实现思路稍微有些出入，代码是high游标先移动且low游标从第一个位置开始移动，用一个临时变量保存第一个元素的值

最优时间复杂度： O(nlogn)
    从代码看不好直接看出时间复杂度，可以分析其过程得到时间复杂度
    每次分裂的子序列恰好排好2个元素，就是每次恰好都是在中间将序列分成两部分，这个时候的排序是最优时间复杂度
        要将序列分裂x次；第一次分裂可以排好一个元素，第二次分裂可以排好2个元素...第x次分裂可以排好2^x个元素
            根据等比数列公式1*(1-2^x)/(1-2) = n --> x = log2(n+1)      -- 有log2(n+1)个行
        对于分裂后的子序列来说，需要移动游标n次才能将这些子序列的第一个元素排好  -- 每一行执行n次游标移动
        最终时间复杂度是是O(nlogn)
最坏时间复杂度： O(n^2)
    每次分裂的子序列恰好排好一个元素,每次都将第一个元素移动到最后

稳定性: 不稳定

不需要额外的空间

"""


def quick_sort(li, start, end):
    if start >= end:
        return
    low_index = start
    high_index = end
    first_value = li[start]
    while low_index < high_index:
        while low_index < high_index and li[high_index] >= first_value:  # high_index游标向前移动; "="是将等于的值都放到子序列一边
            high_index -= 1
        li[low_index] = li[high_index]  # 将li[high_index]的值放在li[low_index]
        while low_index < high_index and li[low_index] < first_value:  # low_index游标向后移动
            low_index += 1
        li[high_index] = li[low_index]  # 将li[low_index]的值放在li[high_index]
    li[low_index] = first_value  # 退出大循环，此时low_index = high_index
    if low_index - 1 - start > 0:  # 只要左边元素个数大于2，还要执行快速排序
        quick_sort(li, start, low_index - 1)
    if end - (high_index + 1) > 0:  # 只要右边元素个数大于2，还要执行快速排序
        quick_sort(li, high_index + 1, end)


def main():
    li = [3, 48, 2, 7, 1, 12, 37, 0, 4, 4, 11]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)


if __name__ == "__main__":
    main()
