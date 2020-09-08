"""
算法是独立存在的一种解决问题的方法和思想
对于算法而言，实现的语言并不重要，重要的是思想
"""

import time

time_start = time.time()
for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if a + b + c == 1000 and a * a + b * b == c * c:
                print(a, b, c)
time_end = time.time()

print("总用时：", time_end - time_start)
