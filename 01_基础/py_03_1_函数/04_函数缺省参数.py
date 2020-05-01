"""
就是给函数参数设置默认值,调用此函数时,不传入该参数的话,就使用该参数的默认值

缺省参数应当是大多数的入参都是此值

注意事项:
    1.缺省参数应放在参数列表末尾
    2.当一个函数有多个缺省参数时,调用时需要指定参数名,防止传递错误
"""


def print_info(name, age=100, is_girl=True):  # 大概率是女生的话,缺省参数就设为True
    gender_info = "女生"
    if not is_girl:
        gender_info = "男生"
    print("name=%s, age=%d,gender=%s" % (name, age, gender_info))


name = "小美"
print_info(name)  # 不传入第二个参数的话,函数就默认使用默认值

name = "小明"
# print_info(name, False)#如果不指定参数名的话,False就会传递给age
print_info(name, is_girl=False);
