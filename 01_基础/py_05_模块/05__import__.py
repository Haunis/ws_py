"""
__import__(字符串模块名):
    解析字符串，并将该字符串当作模块名导入，和import 模块名一致
"""
import cat_module as ca

print(ca)

ret_module = __import__("cat_module")  # 导入cat_module
print(ret_module)  # 和ca结果一样

fun = getattr(ret_module, "say_hello")  # 获取指定模块里的函数名
fun()
