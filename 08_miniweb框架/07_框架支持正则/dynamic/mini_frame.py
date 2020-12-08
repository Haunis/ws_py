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
@route(r"index.html")
def index(matcher):
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
                    systemidvalue="%s">
            </td>
        </tr>
    """
    tr = ""
    for line in all_data:
        tr += tr_template % (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[1])
    content = re.sub(r"\{%content%\}", tr, content)
    return content


@route(r"center.html")
def center(matcher):
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
                       href="/update/%s.html">
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
                        systemidvalue="%s"
                    >
               </td>
           </tr>
       """
    tr = ""
    for line in all_data:
        tr += tr_template % (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[0], line[0])
    content = re.sub(r"\{%content%\}", tr, content)
    return content


@route(r"^add/([^\.]+)\.html")
def add_focus(matcher):
    code = matcher.group(1)
    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='web_data',
                       charset='utf8')
    cur = conn.cursor()

    # 1.查询数据库中是否有该记录
    sql_sentence = "select * from info where code=%s"
    count = cur.execute(sql_sentence, code)
    ret = cur.fetchone()
    if not ret:  # 无记录，则返回
        cur.close()
        conn.close()
        return "无该条记录：%s" % code

    # 2.查询是否已经自选
    # sql_sentence = "select * from focus where info_id=(select id from info where code='%s');"
    sql_sentence = "select * from info as i inner join focus as f on i.id=f.info_id having i.code=%s;"
    count = cur.execute(sql_sentence, code)
    ret = cur.fetchone()
    if ret:  # 已经自选了，则告知不在自选
        cur.close()
        conn.close()
        return "%s 已经自选,无需再次添加!!!" % code

    # 3.有记录且无自选则在关注里插入该条数据
    sql_sentence = "insert into focus (info_id) select id from info where code = %s;"
    count = cur.execute(sql_sentence, code)
    conn.commit()
    cur.close()
    conn.close()
    return "加入自选成功:%s" % code


@route(r"^del/([^\.]+)\.html")
def del_focus(matcher):
    code = matcher.group(1)
    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='web_data',
                       charset='utf8')
    cur = conn.cursor()

    # 1.查询数据库中是否有该记录
    sql_sentence = "select * from info where code=%s"
    count = cur.execute(sql_sentence, code)
    ret = cur.fetchone()
    if not ret:  # 无记录，则返回
        cur.close()
        conn.close()
        return "无该条记录：%s" % code

    # 2.查询是否已经自选
    # sql_sentence = "select * from focus where info_id=(select id from info where code='%s');"
    sql_sentence = "select * from info as i inner join focus as f on i.id=f.info_id having i.code=%s;"
    count = cur.execute(sql_sentence, code)
    ret = cur.fetchone()
    if not ret:  # 未在自选,则告知client无需删除
        cur.close()
        conn.close()
        return "未在自选：%s" % code

    # 3.有记录且自选,则在关注里删除该条数据
    sql_sentence = "delete from focus where info_id =(select id from info where code = %s);"
    count = cur.execute(sql_sentence, code)
    conn.commit()
    cur.close()
    conn.close()
    return "已删除自选:%s" % code


# @route(r"update/([^\.]+)\.html") #error 这个正则会匹配到 update/603993/值的购买.html
@route(r"update/(\w+)\.html")  # update/300286.html
def show_update_page(matcher):
    code = matcher.group(1)
    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='web_data',
                       charset='utf8')
    cur = conn.cursor()
    with open("./templates/update.html") as f:
        content = f.read()
    sql_sentence = "select f.note_info from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"
    # sql_sentence = "select note_info from focus where info_id=(select id from info where code = %s);"
    count = cur.execute(sql_sentence, code)
    one_data = cur.fetchone()  # one_data是个元组
    comment = one_data[0]
    content = re.sub(r"\{%note_info%\}", comment, content)  # 将content里的{%note_info%}用查到的数据替换掉
    content = re.sub(r"\{%code%\}", code, content)
    cur.close()
    conn.close()

    return content


@route(r"update/(\w+)/(\w+)\.html")  # update/603993/值的购买.html
def update_comment(matcher):
    code = matcher.group(1)
    comment = matcher.group(2)

    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='web_data',
                       charset='utf8')
    cur = conn.cursor()
    sql_sentence = "update focus set note_info = %s where info_id = (select id from info where code=%s);"
    count = cur.execute(sql_sentence, (comment, code))

    conn.commit()
    cur.close()
    conn.close()
    return "修改成功!!!"


# env['FILE_PATH']: index.html,center.html, add/008.html
def application(env, start_response):
    if start_response:
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])  # 回调,返回header
    file = env['FILE_PATH']

    if len(file) == 0:
        return "欢迎来到主页---------time:%s" % time.ctime()  # 返回body
    else:
        func = matcher = None
        for url_pattern, fun in g_func_dict.items():
            ret = re.match(url_pattern, file)
            if ret:  # 字典里有存储该file对应的函数
                print("===>ret:", ret)
                func = fun
                matcher = ret
                break
        try:
            return func(matcher)
        except Exception as e:
            # LogUtils.e("无该文件:%s" % file)
            # LogUtils.e("error:%s" % str(e))
            print("无该文件:%s" % file)
            return "无文件: %s--------现在时间是:%s" % (file, time.ctime())


if __name__ == "__main__":
    application({"FILE_PATH": "update/000007/aaa.html"}, None)
