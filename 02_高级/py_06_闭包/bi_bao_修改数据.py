def outter():
    x = 100

    def inner():
        nonlocal x
        print("before x = %s" % x)
        x = 200  # 会直接修改x的值,nonlocal和global作用相似
        print("after x = %s" % x)

    return inner


fun = outter()
fun()

fun()  # 这次使用闭包里数据已经被修改
