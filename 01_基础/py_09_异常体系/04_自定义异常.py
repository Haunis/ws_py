"""
自定义异常两步即可完成:
    1.使用Exception创建新对象
    2.使用raise抛出异常

"""


def input_passwd():
    passwd = input("please input password:")
    if len(passwd) >= 8:
        return passwd
    else:
        ex = Exception("密码长度小于8")
        raise ex
        return None


try:
    print("passwd:%s" % input_passwd())
except Exception as ex:
    print(ex)
