"""
import用法:
from x_module import arg #从x_module加载arg,并且arg指向x_module里的arg的值的内存地址
from x_module import *
from x_module import arg1,arg2
import x_module as X
import x_module #两个作用:1.加载x_module.py 2.变量x_module指向x_module.py这个模块

import搜索路径:
    1.import sys
    2.print(sys.path) # 这个结果就是import模块的搜索路径(包括当前路径)
添加sys.path搜索路径:
   方法一:sys.path.append("/home/user/xxx") #添加到最后
   方法二:sys.path.insert(0,"/home/user/xxx") #添加到最前

import有防止重导入机制,比如导入一个模块3次,只有第一次生效

如果有重新导入的需求,比如更改了模块里的内容,但程序不可停止
可以imp模块里的reload,使用reload之前该模块必须原先已经import:
    1.from imp import reload
    2.reload(x_module)
"""
import change_module  # 虽然飘红，但正常运行
import print_module


def main():
    change_module.change_common()
    print_module.print_data()


if __name__ == "__main__":
    main()
