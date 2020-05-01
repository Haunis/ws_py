"""
模块的搜索顺序:先从当前目录搜索,未搜索到再从系统目录搜索

查看模块完整路径: 每个模块都有__file__内置属性保存其完整路径

"""

import random
from py_05_模块 import cat_module

num = random.randint(0, 10)
print(num)
print("%s" % random.__file__)  # /usr/lib/python3.6

print("cat_module 路径: %s" % cat_module.__file__)
