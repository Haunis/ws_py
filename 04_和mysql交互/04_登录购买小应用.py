#! /usr/bin/python3
"""
python和mysql交互小demo
实现登录、注册、购买、购买后订单写入订单数据库
"""
import pymysql
import datetime


class MySqlProxy(object):
    def __init__(self):
        # 1.链接
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='jing_dong',
                                    charset='utf8')
        # 2.获取cursor
        self.cursor = self.conn.cursor()
        self.customer_id = None

    def run(self):
        while True:
            print("请输入功能：")
            print("1.查询所有商品信息")
            print("2.购买商品")
            print("exit: 退出")
            opt = input()
            if opt == "1":
                self.show_all()
            elif opt == "2":
                self.buy_goods()
            elif opt == "exit":
                break
            else:
                print("请输入正确功能")

    def execute_and_print(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for temp_data in data:
            print(temp_data)

    def show_all(self):
        sql = "select * from goods"
        self.execute_and_print(sql)

    def buy_goods(self):
        ret = 1
        if self.customer_id is None:
            print("未登录")
            ret = self.login_or_register()
        if ret > 0:
            goods_id = input("请输入要购买的商品id:")
            sql = "select * from goods where id='%s'" % goods_id
            count = self.cursor.execute(sql)
            if count == 1:
                print("购买成功")
                str_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                sql = "insert into orders (order_date_time,customer_id)values('%s','%s')" % (str_time, self.customer_id)
                print(sql)
                self.cursor.execute(sql)

                sql = "select id from orders where customer_id='%s'" % self.customer_id
                print(sql)
                self.cursor.execute(sql)
                data = self.cursor.fetchone()
                print("查询到的结果：", data)
                order_id = data[0]
                sql = "insert into order_detail (order_id,goods_id,quantity)values(%d,%d,%d)" % (
                    int(order_id), int(goods_id), 1)
                print(sql)
                self.cursor.execute(sql)

                self.conn.commit()
            else:
                print("无该商品")

    def login_or_register(self):
        while True:
            ret = -1
            opt = input("请选择登录【1】或者注册【2】,返回上一级【0】：")
            if opt == "1":
                ret = self.login()
                if ret == 1:
                    return ret
            elif opt == "2":
                self.register()
            elif opt == "0":
                return -1
            else:
                print("请输入正确的功能")

    def login(self):
        name = input("请输入您的姓名：")
        passwd = input("请输入您的密码：")
        sql = "select * from customer where name='%s'and passwd='%s'" % (name, passwd)
        print(sql)
        count = self.cursor.execute(sql)
        if count == 1:
            print("登录成功!!!")
            sql = "select id from customer where name='%s'" % name
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            print("登录后获取customer_id:", data)
            self.customer_id = data[0]
            return 1
        else:
            print("用户名或密码错误！！！")
            return -1

    def register(self):
        name = input("请输入您的姓名：")
        sql = "select * from customer where name='%s'" % name
        # print(sql)
        count = self.cursor.execute(sql)
        if count == 1:
            print("该名字已被使用")
            return -1
        else:
            passwd = input("请输入密码：")
            tel_num = input("请输入手机号：")
            address = input("请输入地址：")
            sql = "insert into customer (name,passwd,tel_num,address)values ('%s','%s','%s','%s')" % (
                name, passwd, tel_num, address)
            print(sql)
            count = self.cursor.execute(sql)
            self.conn.commit()
            if count == 1:
                print("注册成功!!!!")
                return 1

    def __del__(self):
        self.conn.close()
        self.cursor.close()


def main():
    sqlProxy = MySqlProxy()
    sqlProxy.run()


if __name__ == "__main__":
    main()
