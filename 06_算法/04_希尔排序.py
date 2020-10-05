"""
shell sort:希尔排序； 是对插入排序的改良,与普通插入算法的区别就是有gap

实现思想：取一个步长gap如4,将原序列按照每gap个元素分成几个子序列，这几个子序列组成一个矩阵(gap个列)，对这个矩阵的列进行排序(插入排序)
        将gap降小，如gap取2，继续对矩阵进行列排序(使用插入排序)。
        将gap取1，再对序列进行插入排序;(gap取1就是插入排序)

        也可以认为，每隔gap取一个元素，对这些元素使用插入排序

平均时间复杂度：O(nlogn)~O(n^2)
最坏时间复杂度:O(n^2)
最优时间复杂度:跟gap有关，gap的取值由相关数学算法算出来; 统计上来看是O(n^1.3)
稳定性：不稳定;  有gap的存在，分成了几部分，所以元素的位置可能会变
"""


# 希尔排序;从gap开始，每个元素都向本列前面插入;可以和插入排序代码比较来看
def shell_sort1(li):
    gap = len(li) // 2
    while gap > 0:
        print("------------------sort1,gap:%s--------------" % gap)
        for i in range(gap, len(li)):
            # print(".........", i)
            for j in range(i, 0, -gap):
                # print(j)
                if j - gap >= 0 and li[j] < li[j - gap]:  # 注意要有 >=0 判断，否则list索引可以取负值
                    li[j], li[j - gap] = li[j - gap], li[j]
                else:  # 如果插入的元素恰好最大;这个是希尔排序能够实现优化的关键
                    break
        print("gap=%s排序后:" % gap)
        print_list(li, gap)
        gap //= 2


# 希尔排序; 对每一列进行操作;两个方法其实效果一样的，都是从gap开始，后面每个元素向本列前面插入
# 这个方式理解起来更方便，但是实现麻烦
def shell_sort2(li):
    gap = len(li) // 2
    while gap > 0:  # gap是多少就是有多少列
        print("------------------gap:%s--------------" % gap)
        for column in range(gap):  # 对每一列进行插入排序，从第0列开始
            row = len(li) // gap  # 整除是//; python2中是 /
            if column + 1 + row * gap <= len(li):  # 某些列会多一行
                row = row + 1
            # 开始插入排序;
            # 默认每一列第1个元素(索引column)有序，后续每列元素向前插入; 索引column + gap为每一列第2个元素
            for i in range(column + gap, column + row * gap, gap):
                for j in range(i, column, -gap):
                    # print("j =", j)
                    if li[j] < li[j - gap]:
                        li[j], li[j - gap] = li[j - gap], li[j]
                    else:  # 如果插入的元素恰好最大
                        break
            print("第%s列排序后" % column)
            print_list(li, gap)
        gap //= 2


def print_list(li, gap):
    count = 0
    for ele in li:
        count += 1
        print(ele, end="\t")
        if count % gap == 0:
            print()
    print()


def main():
    li = [111, 48, 81, 47,
          12, 6, 18, 23,
          22, 14, 7, 57,
          9]

    print_list(li, len(li) // 2)
    shell_sort1(li)
    print(li)


if __name__ == "__main__":
    main()
