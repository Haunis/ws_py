#! /usr/bin/python3

"""
算法是独立存在的一种解决问题的方法和思想
对于算法而言，实现的语言并不重要，重要的是思想

时间复杂度:就是执行总基本数和算法规模N的关系

渐进函数:
    对于单调的整数函数f,如果存在一个整数函数g和常数c,使得对于充分大的n总有f(n)<=c*g(n),
    就称函数g是f的渐进函数(忽略常数),记为f(n)=O(g(n));
    在趋向无穷极限的意义下,函数f的增长受到函数g的约束,亦即函数f和函数g的特征类似
    例如:f(n) = g(n)*2;

问题引入:已知 a,b c是自然数,且a+b+c = 1000; a*a +b*b = c*c,求a,b,c
"""

import time


# 算法1:枚举全部,大概2分钟
def algorithm_1():
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print("算法1:", a, b, c)
    """
    每台机器执行的总时间不同,但执行基本运算数量大体相同
    以该算法为例,执行的总基本数为:
        T = 1000*1000*1000*2
    如果题目条件 是a+b+c =2000的话: 
        T = 2000*2000*2000*2
    如果算法a+b+c=N,N称为算法规模
        T = N*N*N *2
        记T(n) = g(n)*2,g(n)=N*N*N
        其中g(n)=N^3,是T(n)的渐进函数
        
    """


# 算法2: 只枚举a,b,而c用1000-a-b表示; 大概0.38s
def algorithm_2():
    for a in range(1001):
        for b in range(1001):
            c = 1000 - a - b
            if c >= 0 and a ** 2 + b ** 2 == c ** 2:
                print("算法2:", a, b, c)
    """
    T(n)=n*n*2
    g(n)=n^2
    """


def main():
    time_start = time.time()
    # algorithm_1()
    algorithm_2()
    time_end = time.time()
    print("总用时：", time_end - time_start)


if __name__ == "__main__":
    main()
