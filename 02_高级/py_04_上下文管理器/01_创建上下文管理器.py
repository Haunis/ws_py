"""
上下文
    上文:程序执行代码需要知道执行前所需的相关数据
    下文:程序执行完之后,将相关数据保存起来

创建上下文管理器有两种方式:
    方式一:实现 __enter__()和__exit__()方法的类,该类就是上下文管理器
    方式二:使用contextlib库

with就是执行上下文管理器的
"""

from contextlib import contextmanager


# 方式一:
class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("File enter ...")
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("File exit ...")
        self.file.close()


# 方式二:
@contextmanager
def file_open(name, mode):
    f = open(name, mode)
    print("file_open before")
    yield f  # with file_open()会得到该f
    f.close()  # with执行完会自动调用该代码
    print("file_open after")

print("-------------with File----------------");
with File("test.txt", "w") as f:  # f就是 __enter__()返回的值
    f.write("hhhh")

print("-------------with file_open----------------");
with file_open("test.txt", "a") as f:
    f.write("\nfile_open")
