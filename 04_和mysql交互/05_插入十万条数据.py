import pymysql as sql


def main():
    # 1.链接
    conn = sql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='jing_dong',
                       charset='utf8')
    # 2.获取cursor
    cur = conn.cursor()
    # 3.执行sql语句
    count = cur.execute("create table if not exists test_index(title varchar(20))")
    for num in range(100000):
        cur.execute("insert into test_index value ('haha%d')" % num)

    conn.commit()
    # 4.关闭
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
