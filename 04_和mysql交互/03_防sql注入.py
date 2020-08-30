"""
不要自己拼接sql语句

使用pymysql自带的拼接方法可以一定程度上防止注入
cursor.execute(sql,arg)

"""

import pymysql


def main():
    # 1.链接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='haunis', password='haunis', database='jing_dong',
                           charset='utf8')
    # 2.获取cursor
    cursor = conn.cursor()
    # 3.执行sql语句
    while True:
        print("查询某个商品的信息")
        brand_name = input("请输商品名(exit to exit):")  # 如: "商务双肩背包"
        if brand_name == "exit":
            break
        else:
            # sql = "select * from goods where name='%s'"%brand_name  # 自己组装的语句输入: 'or 1=1 or'就会查询所有
            # print(sql);
            # count = cursor.execute(sql)

            arg = [brand_name] #需要传几个参数，数组里就放几个且sql语句就必须有几个%s
            count = cursor.execute('select * from goods where name=%s', arg)  # 使用python自带的可以一定程度上避免注入
            ret = cursor.fetchall()
            for temp in ret:
                print(temp)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
