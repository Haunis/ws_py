"""
高级数据类型公共方法:
    1.内置函数(就是不需要导包的函数)
        a.len(item)
        b.del(item) 还有一种用法 del item,这两种用法效果一样
        c.max(item)
        d.min(item)
        e.cmp(item1,item2)
            在python3中比较可以使用比较运算符 >或者<，字典不可以使用运算符比较大小
            比较运算符比较字符串时，逐一比较字符，如"abc"<"baa"为True
            对列表和元组也可以使用切片，字典不可以使用切片
    2.切片(截取)
        字典不可以使用切片,因为字典是无序的
    3.运算符
        + : 字典不可使用
        * : 字典不可使用
        in : 字典使用的话,判断的是key; 也叫成员运算符
        not in : 字典使用的话,判断的是key; 也叫成员运算符
"""
list_num = [1, 2, 3, 4]
print("list_num:%s" % list_num)
print("list_num*2:%s" % (list_num * 2))

str1 = "aaa"
str2 = "bbb"
print("str1 = %s\nstr2 = %s\nstr1+str2 = %s" % (str1, str2, str1 + str2))
