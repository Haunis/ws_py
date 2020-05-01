"""
包是一个包含多个模块的特殊目录,里面包含一个特殊文件__init_.py
定义包的好处: import 包名 可以使用包里所有的模块

__init__.py作用:指定对外界提供的模块列表

只可以在包里的__init__.py使用"from ." 其他地方使用 from . 会报错
"""

from . import cat
from . import dog
