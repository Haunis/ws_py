"""
匿名函数
"""


def foo():
    print("foo called")


# foo重新指向了另外一个函数
foo = lambda x: x + 1

ret = foo(1)
print(ret)  # 最终结果是2
