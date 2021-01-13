"""
相邻元素挨个比较,一轮比较下来最大的放最后,下一轮最大的放倒数第二位置...
时间复杂度O(n^2)，如果是有序的话，可以优化,优化后时间复杂度是O(n)

稳定性：稳定
"""

li = [3, 48, 2, 7, 1, 12, 37, 0, 4, 11]

print(li)
for i in range(len(li) - 1, -1, -1):
    is_switch = False  # 优化，如果原本就是有序的，则时间复杂度是O(n)
    for j in range(i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
    if is_switch == False:
        break
print(li)
