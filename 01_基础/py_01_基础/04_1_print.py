"""
print()可用两种输出方式
    1.不适用占位符,直接逗号后面跟变量输出
    2.使用占位符,和C语言使用类似,但是变量和字符串之间用%隔开
%d 输出整数
%f 输出浮点型
%s 输出字符串
%% 输出%
%#x 输出内存地址,和c一样

print()默认是换行的,改成print(args,end="")可实现不换行输出
"""

name = "Lee"
age = 12
height = 175.23333
isMale = True

print("age = %06d" % age)  # 000012  06d的意思是如果正数不到6位,前面用0补齐,如果超过6位,该是多少就是显示多少

print("name=", name, "age=", age, "height=", height, "isMale=", isMale)

print("name=%s,age=%d, height=%.2f,isMale=%s" % (name, age, height, isMale))

print("*", end="")  # 实现不换行
print("*", end="----")  # "*"后面跟"----"
