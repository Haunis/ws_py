"""
python和RDBMS(关系型数据库，常见的有mysql,oracle)通信需要借助第三方库

安装pymysql:
    pip3 install pymysql;

python通过pymsql和mysql交互一般流程：
    1.链接： conn=connect()
    2.获取cursor: cur=conn.cursor()
    3.进行操作: cur.exec(sql语句)
    4.关闭链接: conn.close()
    5.关闭cursor: cur.close()

在python中操作mysql,是默认开启事务的
如果只是查数据,不需要commit;如果是增删改,需要commit提交
"""
import pymysql as sql


def main():
    # 1.链接
    conn = sql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='jing_dong',
                       charset='utf8')
    # 2.获取cursor
    cur = conn.cursor()
    # 3.执行sql语句
    count = cur.execute("select * from goods")
    print("count:", count)
    one_data = cur.fetchone()  # 只取第一行，是个元组
    many_data = cur.fetchmany(3)  # 接着取3行;元组里放3个元组
    all_data = cur.fetchall()  # 取剩下的全部；all_data是一个元组，元组里每个item也是元组

    print("-------------------one_data------------------------")
    print(one_data)
    print("\n-------------------many_data------------------------")
    for temp in many_data:
        print(temp)
    print("\n-------------------all_data------------------------")
    for temp in all_data:
        print(temp)

    # 4.关闭
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
