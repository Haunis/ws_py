"""
该文件作为应用程序框架
要让浏览器正切解析中文,要在回复头中添加:charset=utf-8
"""
import time


def index():
    with open("./templates/index.html") as f:
        content = f.read()
    return content


def center():
    with open("./templates/center.html") as f:
        return f.read()


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])  # 回调,返回header
    file = env['FILE_PATH']
    if file == "center.py":
        return center()
    elif file == "index.py":
        return index()
    elif len(file) == 0:
        return "欢迎来到主页---------time:%s" % time.ctime()  # 返回body
    else:
        return "支持 WSGI---------time:%s" % time.ctime()  # 返回body
