"""
if 可以判断 数字，字符串，列表，元组
数字： 0-False, 非0-True
字符串，列表，元组字典： 不是空成立
不是None成立
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
if not None:
    print("not None ok")
