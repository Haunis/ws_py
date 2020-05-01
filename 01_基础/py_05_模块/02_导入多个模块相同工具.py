"""
不同模块导入重名工具时,后导入的会把先导入的覆盖
如果确实有需求要这样做的话,可以给工具起别名

"""
# from dog_module import say_hello
from dog_module import say_hello  # 后导入的say_hello会把先导入的say_hello覆盖
from cat_module import say_hello as cat_say_hello  # 起别名

say_hello()
cat_say_hello()
