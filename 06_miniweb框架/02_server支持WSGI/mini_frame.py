"""
该文件作为应用程序框架
要让浏览器正切解析中文,要在回复头中添加:charset=utf-8
"""
import time


def login():
    return "登录页---------time:%s" % time.ctime()


def register():
    return "注册页---------time:%s" % time.ctime()


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])  # 回调,返回header
    file = env['FILE_PATH']
    if file == "login.py":
        return login()
    elif file == "register.py":
        return register()
    else:
        return "支持 WSGI---------time:%s" % time.ctime()  # 返回body
