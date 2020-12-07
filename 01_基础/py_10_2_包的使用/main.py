#! /usr/bin/python3
"""
使用:
    1.导包: import 包名
    2.使用: 包名.模块名.工具名

"""
import sys
sys.path.append("../")

#和from . import dog配合使用
# import py_10_1_定义一个包 as my_package
# my_package.dog.run()
# my_package.cat.run()

#和 __all__ = ['cat', 'dog']配合使用
from py_10_1_定义一个包 import *
dog.run()