#! /usr/bin/python3


"""
增删改都涉及到更改数据库，所以要commit之后才能将数据同步到数据库文件

在commit之前，可使用rollback()取消掉cursor.excute()执行的更改操作，但是执行execute之后数据表的主键就会修改--防止并发
"""
import pymysql


class MySqlProxy(object):
    def __init__(self):
        # 1.链接
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='jing_dong',
                                    charset='utf8')
        # 2.获取cursor
        self.cursor = self.conn.cursor()

    def run(self):
        while True:
            opt = input("\n请输入功能：\n1.查询所有商品信息\n2.查询所有商品分类\n3.查询所有商品品牌\n4.插入一条品牌\nexit: 退出\n")
            if opt == "1":
                self.show_all()
            elif opt == "2":
                self.show_all_cate()
            elif opt == "3":
                self.show_all_brand()
            elif opt == "4":
                self.insert_brand()
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

    def show_all_brand(self):
        # sql = "select b.name from goods_brand as b inner join goods as g on b.id=g.brand_id group by b.name";
        sql = "select * from goods_brand"
        self.execute_and_print(sql)

    def show_all_cate(self):
        sql = "select c.name from goods_cate as c inner join goods as g on c.id=g.cate_id group by c.name";
        self.execute_and_print(sql)

    def insert_brand(self):
        new_brand = input("请输入新品牌：")
        sql = """insert into goods_brand (name)values("%s")""" % new_brand  # 执行insert之后，无论commit与否，表的主键都会修改--为防止并发修改数据表
        self.cursor.execute(sql)
        # self.conn.rollback() #commit之前都可以回滚
        self.conn.commit()  # 需要提交才能将数据写入数据库

    def __del__(self):
        self.conn.close()
        self.cursor.close()


def main():
    sqlProxy = MySqlProxy()
    sqlProxy.run()


if __name__ == "__main__":
    main()
