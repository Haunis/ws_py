"""
文件和目录的常用操作都是通过python自带的os模块实现的

文件操作
os.rename(src,dest)     重命名文件
os.remove(file)         删除文件

目录操作
os.listdir(dir)     目录列表
os.mkdir(dir)       创建目录
os.rmdir(dir)       删除目录
os.getcwd()         获取当前目录
os.chdir(dest_dir)  修改目录
os.path.isdir(dir) 是否是文件夹
os.path.isfile(file) 是否是文件夹

文件和目录都支持相对路径和绝对路径
"""
import os

print("os.__file__: %s" % os.__file__)
print("os.__name__: %s" % os.__name__)

print(os.listdir("."))
print("aaa is_dir:%s " % os.path.isdir("./dddd"))
print("abc.txt is file:%s" % os.path.isfile("abc.txt"))
# os.chdir()
file_list = os.listdir(".")  # 返回一个数组


