def get_decorator(func):
    def decorator(num):
        print("decorator called")
        func(num)

    return decorator


@get_decorator  # 语法糖； 等价于 test = get_decorator(test)
def test(num):
    print("test called,num=%d" % num)


test(11)
