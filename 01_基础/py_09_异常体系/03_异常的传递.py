"""
当函数出现异常时,程序并不会立即停止.
函数会将异常传递给函数的调用处,这样依次向上层层传递,最终没有处理这个异常程序才会停止

利用异常的传递性,可以在主程序中捕获异常;这样就不用在每个函数里增加大量异常捕获
"""


def demo1():
    return int(input("请输入一个整数:"))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as e:
    print("e : %s" % e)
