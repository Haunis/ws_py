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
os.path.isdir(file) 是否是文件

文件和目录都支持相对路径和绝对路径
"""
import os

print(os.__file__)
print(os.__name__)

print(os.listdir("."))  # 返回一个数组
print(os.path.isdir("./abc.txt"))
os.chdir()
os.chdir()
