"""
该文件作为应用程序框架
要让浏览器正切解析中文,要在回复头中添加:charset=utf-8

带参数的装饰器:用返回的函数作为装饰器
"""
import time
import LogUtils
import re
import pymysql as sql

g_func_dict = dict()


def route(file_name):
    def set_func(func):
        g_func_dict[file_name] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


# 相当于2步:
#   1.set_func = put_in_dict("index.html")
#   2.index = set_func(index)
@route("index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()
    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='web_data',
                       charset='utf8')
    cur = conn.cursor()
    count = cur.execute("select * from info")
    all_data = cur.fetchall()
    cur.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input 
                    type="button" 
                    value="添加" 
                    id="toAdd"
                    name="toAdd"
                    systemidvalue="000007"
                >
            </td>
        </tr>
    """
    tr = ""
    for line in all_data:
        tr += tr_template % (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
    content = re.sub(r"\{%content%\}", tr, content)
    return content


@route("center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()
    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='web_data',
                       charset='utf8')
    cur = conn.cursor()
    count = cur.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info "
                        "from info as i inner join focus as f on i.id=f.info_id;")
    all_data = cur.fetchall()
    cur.close()
    conn.close()

    tr_template = """
           <tr>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>
                    <a type="button" 
                       class="btn btn-default btn-xs"
                       href="/update/300268.html">
                       <span
                            class="glphicon glphicon-start"
                            aria-hidden="true">
                       </span>
                       修改
                    </a>
               </td>
               <td>
                    <input 
                        type="button" 
                        value="删除" 
                        id="toDel"
                        name="toDel"
                        systemidvalue="300268"
                    >
               </td>
           </tr>
       """
    tr = ""
    for line in all_data:
        tr += tr_template % (line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    content = re.sub(r"\{%content%\}", tr, content)
    return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])  # 回调,返回header
    file = env['FILE_PATH']

    if len(file) == 0:
        return "欢迎来到主页---------time:%s" % time.ctime()  # 返回body
    else:
        try:
            func = g_func_dict[file]
        except Exception as e:
            LogUtils.e("keyerror:" + str(e))
            return "无文件: %s--------现在时间是:%s" % (file, time.ctime())
        else:
            return func()
