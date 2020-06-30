#! /usr/bin/python3
# -*-coding:utf-8-*-
"""
正则应用场景:
    1.匹配输入数据是否符合要求
    2.爬虫时,匹配想要的数据

正则表达式就是一个字符串

匹配一个字符
[]  --[abc]表示a,b或者c 
    --[1-8]表示1~8
    --[1-36-8]表示1~3,6~8
\d  --匹配一位数字0~9,如abc\d,则abc1,ab2都匹配




"""

import re

print("------------------定义-------------------------")
rex = r"hello"  # 定义一个匹配hello开头的正则字符串

ret = re.match(rex, "sello")  # 匹配成功就返回一个对象,失败就无返回
print(ret)
if ret is not None:
    print(result=ret.group())  # gropu()取出匹配的结果

print("------------------1.严格匹配字符串-------------------------")
ret = re.match(r"abc", "abc")
print(ret)

print("------------------2.匹配数字\d-------------------------")
ret = re.match(r"abc\d", "abc33")  # abc0~abc9都行,abc99999也行,但只能匹配出abc9
print(ret)

print("------------------3.匹配多个[]-------------------------")
ret = re.match(r"abc[dD]", "abcd")  # abcd abcD都行
print(ret)
