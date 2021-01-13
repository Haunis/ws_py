"""
用的比较少
背景知识：
    将一个有序序列A和一个有序序列B合并成一个有序序列C(假设A B C 顺序都是由小到大)
    1.假设有两个指针p_a和p_b分别指向A和B的第一个元素。比较p_a和p_b指向的元素，谁小就将谁放入C的第一个位置，且将指针向后移动一个位置
    2.继续比较指针指向的元素，将小的元素放入C的第二个位置，指针继续移动
    3.重复1 2 ，直至A和B所有的元素都放入C，这个时候C中的元素就是有序的
    证明：每次放入C中的元素都是两个序列A和B指针指向的元素及其后面的元素中最小的元素，所以最终的C是有序的


归并排序：
    将序列分裂：
    1.将序列从中间一分为二，分成长度相等的两个子序列(如果序列长度为奇数的话，后半部分的子序列长度比前半部分多1)
    2.将子序列继续一分为二...直至所有子序列的长度都为1
    将序列合并：
    3.将长度为1的子序列两两合并，且合并后有大小顺序
    4.将合并后的长度为2的序列继续合并...直至合成一个完整的有序序列

时间复杂度：O(nlogn)  --最坏和最优都是O(nlogn)
    从代码看不好直接看出时间复杂度，可以分析其过程得到时间复杂度
        要分裂/合并 log2(n)次         --有log2(n)个行
        每次合并要执行n次append动作     --每一行执行n次append动作
        最终时间复杂度是O(nlogn)

稳定性：稳定

占用空间较大，需要额外的空间
"""


# 将序列li一分为二，并返回一个有序序列
# 如：li的长度为2，则将li一分为2，然后再合并
# 使用归纳法可证明最终返回的序列一定是个有序序列
def merge_sort(li):
    mid_index = len(li) // 2
    if mid_index <= 0:
        return li
    left_li = merge_sort(li[:mid_index])  # 将左半部分分列、合并成一个新的有序序列
    right_li = merge_sort(li[mid_index:])  # 将右半部分分列、合并成一个新的有序序列

    ret_li = list()  # 要返回的序列
    left_index, right_index = 0, 0  # 就是分别指向两个子序列的指针
    # 执行合并动作
    while left_index < len(left_li) and right_index < len(right_li):
        if left_li[left_index] <= right_li[right_index]:  # <=保证稳定性
            ret_li.append(left_li[left_index])
            left_index += 1
        else:
            ret_li.append(right_li[right_index])
            right_index += 1
    # 退出循环，如果有一个子序列还有元素没有添加到ret_li,则将这些剩下的元素全部添加到ret_li
    # 如果list的长度为4，则list[4:]返回空列表，不会报错
    ret_li.extend(left_li[left_index:])
    ret_li.extend(right_li[right_index:])
    return ret_li


def main():
    li = [3, 48, 2, 7, 1, 12, 37, 0, 4, 4, 11]
    print(li)
    ret_li = merge_sort(li)
    print(li)
    print(ret_li)


if __name__ == "__main__":
    main()
