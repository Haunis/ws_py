"""
send(arg)和next()原理类似,只不过执行yield会得到不同的结果
send(arg)会将参数传给yield,而next()不传参

send(arg)一般在next()之后使用,如果第一次使用的话要传None,即send(None)

"""


def create_num(num_count):
    #####如果第一次启动生成器使用send(None),此处无接收值,send(None)传参也是None,所以不会崩溃
    a, b = 0, 1
    current_num = 0
    while current_num < num_count:
        ret = yield a  # 执行next()会得到此处的a,并且代码会停止在此，等待下一次next()调用
        print("ret>>> ", ret)
        a, b = b, a + b
        current_num += 1
    return "ok"


obj = create_num(10)  # 创建并返回生成器

ret = obj.send(None)  # 如果必须要第一次使用send(arg)的话,参数传None
print("send ret: ", ret)

ret = next(obj)
print("next ret: ", ret)

ret = obj.send("haha")  # send(arg)一般在next()之后使用
print("send ret: ", ret)
