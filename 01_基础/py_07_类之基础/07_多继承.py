"""
如果多个父类存在同名方法,应避免使用多继承

"""


class Fu1:
    def fu1_fun(self):
        print("fu1_fun executed")


class Fu2:
    def fu2_fun(self):
        print("fu2_fun executed")


class Zi(Fu1, Fu2):
    pass


zi = Zi()
zi.fu1_fun()
zi.fu2_fun()
