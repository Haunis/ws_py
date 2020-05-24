"""
模块:
    什么是模块: 每一个以.py结尾的源文件就是一个模块
    命名规则:　模块也是标识符,所以不能命名不能以数字开头(数字,字母,下划线,并且不能以数字开头)
    作用：　模块就好比一个工具包,可以向外界提供全局变量,函数,类
    使用：模块名.变量名　或者　模块别名.变量名

导入模块:
    从子目录导入模块: from subdir1.subdir2 import module
    从模块中导入部分工具: from module import 变量 #导入部分工具可以直接使用,可以不用"模块名.工具名"这种方式调用
    导入所有工具:from module import * #不推荐使用
    导入部分工具时,如果两个模块有相同的函数,后导入的模块会把先导入的模块的函数覆盖.这个时候可以给工具起别名


导入模块时可以起别名
    格式:import xxxmodule as 别名
    别名:要符合大驼峰命名法

导入模块部分工具时也可以起别名
    from xxxmodule import say_hello as my_say_hello

导入模块优先级:
    先从本工程查找，没有找到的话，到系统中找
"""

from py_05_模块 import dog_module as DogModule
# from . import dog_module as DogModule #报错,只可以在包里的__init__.py使用"from ."
from cat_module import Cat  # 可以从模块中导入部分工具; 从子目录导入模块pytcharm会报错,但不影响正常使用
from cat_module import say_hello as cat_say_hello  # 可以给工具起别名

"""
为啥是绿色的....
"""
print("-----------------1.调用模块变量-----------------")
print("DogModule.g_num=%d" % DogModule.g_num)

print("-----------------2.调用模块函数-----------------")
DogModule.multiple_table()

print("-----------------2.调用模块类-----------------")
dog = DogModule.Dog("旺财")
dog.run()
print(dog)

cat = Cat("tom")
cat.run()

cat_say_hello()
