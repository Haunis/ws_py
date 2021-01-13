"""
该文件作为应用程序框架
要让浏览器正切解析中文,要在回复头中添加:charset=utf-8

带参数的装饰器:用返回的函数作为装饰器
"""
import time
import LogUtils

g_func_dict = dict()


def route(file_name):
    def set_func(func):
        g_func_dict[file_name] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


# 相当于2步:
#   1.set_func = put_in_dict("index.py")
#   2.index = set_func(index)
@route("index.py")
def index():
    with open("./templates/index.html") as f:
        content = f.read()
    return content


@route("center.py")
def center():
    with open("./templates/center.html") as f:
        return f.read()


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])  # 回调,返回header
    file = env['FILE_PATH']

    if len(file) == 0:
        return "欢迎来到主页---------time:%s" % time.ctime()  # 返回body
    else:
        func = g_func_dict[file]
        LogUtils.d("func :" + str(func))
        if func:
            return func()
        else:
            return "支持 WSGI---------time:%s" % time.ctime()  # 返回body
