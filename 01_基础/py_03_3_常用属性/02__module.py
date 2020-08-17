"""
__module__:表示当前操作的对象在哪个模块
"""
from test_module import Demo  # 报红,但是可以正常运行

d = Demo()
print(d.__module__)  # test_module
