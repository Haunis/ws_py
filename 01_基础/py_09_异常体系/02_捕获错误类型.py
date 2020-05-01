#! /usr/bin/python3
"""
else: 当try的代码没有异常才会执行
finally:无论如何都会执行

"""
try:
    input_num = int(input("请输入一个被除数："))
    result = 8 / input_num
except ZeroDivisionError:
    print("被除数不可为0")
# except ValueError:
#     print("请输入一个整数")
except Exception as exception:  # 如果上面的异常处理没有进行捕获,就会在此处进行捕获
    print("未知错误: %s" % exception)
else:
    print("else 正常执行")  # 上方没有异常才会执行到这
finally:
    print("finally executed")  # 无论如何都会执行
