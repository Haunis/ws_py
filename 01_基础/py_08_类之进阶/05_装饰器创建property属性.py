# -*-coding:utf-8-*-
"""
使用@property就是使用装饰器创建property属性



property属性:
    定义property属性:
        经典类(python2.x不继承object的类):在方法前加上@property,方法只能有一个参数
        新式类:除了可以@property添加属性外,还可以更改和删除propery属性
    如何使用:
        对象.属性 ,如p.age

作用:
    1.方便开发,如果是调用一个方法还要点进源码进去看传哪些参数;但是property的话就不用传参,使用方式更加简洁
        简化调用者在获取数据的流程
    2.把调用属性的方式转对应成调用方法,从而可以在方法里实现验证等功能

"""


class Goods:
    def __init__(self):
        self.origin_price = 100
        self.discount = 0.8

    @property  # 定义property属性;经典类和新式类都可以
    def price(self):
        print("price called")
        now_price = self.origin_price * self.discount
        return now_price

    @price.setter  # 只能在新式类使用,更改property属性
    def price(self, value):
        print("setter called")
        self.origin_price = value

    @price.deleter  # 只能在新式类时使用,删除property属性
    def price(self):
        print("deleter called")
        del self.origin_price


def main():
    g = Goods()
    g.price  # 调用property属性
    g.price = 200  # 调用@price.setter 对应的
    del g.price  # 调用@price.deleter 对应的


if __name__ == "__main__":
    main()
