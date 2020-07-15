"""
逻辑运算符:and,or,not
not跟的判断: not 条件
not跟的判断: not 条件

条件和条件之间可以用括号()括起来
"""
age = 12
height = 178
print("------------1.and------------------")
if ((age == 12) and height >= 178
        and height >= 178 and height >= 178
        and height >= 178):  # 条件可以用括号括起来
    print("and: ok")
else:
    print("and: not ok")

print("------------2.or------------------")
if age == 12 or height >= 150:
    print("or: ok")
else:
    print("or: not ok")

print("------------3.not------------------")
if not age == 12:
    print("not: ok")
else:
    print("not: not ok")
