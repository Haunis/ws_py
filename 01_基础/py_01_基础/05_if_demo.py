"""
if 可以判断 数字，字符串，列表，元组
数字： 0-False, 非0-True
字符串，列表，元组字典： 不是空成立
不是None成立

is:判断内存地址是否相等
==：判断内容是否相等

参考：https://www.cnblogs.com/ygj0930/p/10942617.html
None 判断使用is
== 运算符是比较对象的值是否相等，原理是调用类的 __eq__函数，而__eq__函数可以被重载
我们可以重载某类的 __eq__ 比较函数，让它总是返回True，则它的实例与None作 == 运算时就为True了。
"""
age = 14
if age == 12:
    print("age = %d" % age)
else:
    print("else executed")

print("-------------------------------------")
season = "spring"
if season == "spring":
    print("season is spring")
elif season == "summer":
    print("season is summer")
elif season == "autumn":
    print("season is autumn")
elif season == "winter":
    print("season is winter")
else:
    print("not know season")

if 1:
    print("1 ok")
if [1, 2]:
    print("list ok")
if (1, 2):
    print("tuple ok")

temp = None
if temp is None:
    print("temp is None")
if temp is not None:
    print("temp is None")