#! /usr/bin/python3
"""
#! 这个符号在linux中叫做shebang 读作she ban ,表示这个文件由那个程序执行
python3 规定所有table键都替换成4个空格,不允许既有table键又有空格
"""

# 单行注释

"""
这是多行注释
"""
print("hello py")

x = 1
y = x
# y = 2
print(id(x))
print(id(y))
