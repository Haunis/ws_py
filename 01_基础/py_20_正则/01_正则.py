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
    --[1-8a-zA-Z]表示1~8,a~z,A~Z
    --[1-8abcd]表示1~8,abcd
\d  --匹配一位数字0~9,如abc\d,则abc1,ab2都匹配
\D  --匹配非数字
\w  -- 0~9,a~z,A~Z,_ 就是数字字母下划线;也可以支持中文,慎用
\W  --匹配非单词字符
\s  --匹配空格,table键(\t),用的少
\S  --匹配非空字符
.   --任意一个字符

{}  --花括号前面的可以重复几次,如
        \d{1,2}就是1个数字或者两个数字
        \d{1,3}从1到3
        \d{11}只能11位
?   --"?"前面的有或者没有,如 "abc-?"匹配abc或者abc-均可




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

print("------------------3.[]匹配多个-------------------------")
ret = re.match(r"abc[dD]", "abcd")  # abcd abcD都行
print(ret)

print("------------------4.匹配\s-------------------------")
ret = re.match(r"abc\t", "abc\tdddd")  # ok
print(ret)

print("------------------5.匹配.-------------------------")
ret = re.match(r"abc.", "abc*dsd")
print(ret)

print("------------------6.{}-------------------------")
ret = re.match(r"abc\d{1,3}", "abc1")  # abc1,abc11,abc111均可
print(ret)

print("------------------7.?-------------------------")
ret = re.match(r"abc-?\d{3,4}", "abc123")  # "-"有没有均可,数字必须3位或者4位
print(ret)
