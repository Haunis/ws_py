"""
列表推导式： temp_list = [x for x in range(10)]

生成器是一个特殊的迭代器
创建生成器方式1： temp = (x for x in range(10)) #注意和列表推导式不同，该处是括号
创建生成器方式2： 函数中有yield语句就是生成器

如果一个函数中有yield,则这个函数不是函数，是生成器模板

生成器特点:
    "函数"执行到yield处,能够暂停执行,并且在下次调用next()或者send()方法时能够恢复执行

"""

print("-------------------创建生成器方式1-------------------------")
temp = (x for x in range(10))
print(temp)

print("-------------------创建生成器方式2-------------------------")


def create_num(num_count):
    print("*****1*****")  # 第一次调用next()时会执行该处代码，第二次调用next()则不会
    a, b = 0, 1
    current_num = 0
    while current_num < num_count:
        # print(a)
        print("*****2*****")
        yield a  # 执行next()会得到此处的a,并且代码会停止在此，等待下一次next()调用
        print("*****3*****")  # 第二次调用next()会从此处开始执行
        a, b = b, a + b
        current_num += 1
        print("*****4*****")


obj = create_num(10)

# 启动迭代器
ret = next(obj)  # 第一次调用next,从create_num()入口处调用
print("ret = ", ret)

ret = next(obj)  # 第二次调用next,从yield后调用
print("ret = ", ret)
