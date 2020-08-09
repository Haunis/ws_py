"""
私有属性和私有方法:
    只可以在类的内部调用,不可在外部调用(子类不可使用父类私有的方法和属性)
    子类对象不能在自己的方法内部直接访问父类的私有属性和私有方法
    定义方式:属性和方法前面加"__"即可


伪私有属性和方法:
    python中并没有真正意义上的私有属性和方法
    python对私有属性和方法的处理方式: 在私有属性和方法前面加上"_类名",如"__age"处理为"_Women__age",所以还是可以访问的
    日常开发中不使用此方式访问私有属性和方法

子类如何访问父类的私有属性和方法:
    调用父类的公有方法,通过父类的公有方法访问父类的私有方法或属性

instance.__dict__ 可以查看对象的所有私有属性

"""


class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __secret(self):  # 私有方法
        print("__secret() name:%s, age:%d" % (self.name, self.__age))  # 在类的内部可以调用私有方法

    def women_pub_fun(self):
        print("父类私有属性 __age=%d" % self.__age)
        self.__secret()


class Daughter(Women):
    def daughter_fun(self):
        # print("访问父类私有属性:%d" % self.__age)#无法访问父类私有属性
        # self.__secret() #不可访问父类私有方法
        # super().__age #不可访问
        self.women_pub_fun()
        pass


xiaomei = Women("小美", 18)
# print(xiaomei.__age) #外界不可访问私有属性
print(xiaomei._Women__age)  # 加上"_类名",强制访问私有属性

# xiaomei.__secret()#外界不可访问私有方法
xiaomei._Women__secret()  # 加上"_类名",强制访问私有方法

print("------------------------------------")
daughter = Daughter("daughter", 18)
daughter.daughter_fun()
