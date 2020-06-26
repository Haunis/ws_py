"""
生成器可以直接使用for循环(因为迭代器本身就是特殊的迭代器)

生成器的启动:
    1.next() 执行后会卡在yield
    2.send() 一般在next()后使用

"""


def create_num(num_count):
    print("*****1*****")  # 第一次调用next()时会执行该处代码，第二次调用next()则不会
    a, b = 0, 1
    current_num = 0
    while current_num < num_count:
        ret = yield a  # 执行next()会得到此处的a,并且代码会停止在此，等待下一次next()调用
        print("ret>>>", ret)  # ret一直为None
        a, b = b, a + b
        current_num += 1
    return "ok"


print("-----------------1.使用for循环-------------------")
obj = create_num(10)
for x in obj:
    print(x)
print("-----------------2.使用while-------------------")
obj2 = create_num(10)
print("iter(obj2): ", iter(obj2))  # <generator object create_num at 0x7fb1be6145c8>
while True:
    try:
        x = next(obj2)  # 该方法会自动调用迭代器的__next__()方法
        print(x)
    except StopIteration as e:
        print("e.value:", e.value)  # e.value保存create_num()return的值
        break
