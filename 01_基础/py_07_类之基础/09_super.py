"""

和java里super稍有不同
java super:
    1.调用构造：super()
    2.调用父类方法：super.fuFunction()
python super:
    super是一个特殊的类,super()就是使用super类创建的对象
    super并不是单纯地调用父类,其调用链由mro决定,所以多继承时,super可能调用不到所有父类
    当然,如果是单继承,super()一定调用其父类

python中调用父类方法:
    方式1: super().fuFunction() #使用当前的类到mro里去寻找,调用其下一个类的方法
    方式2: super(Zi,self).__init()__ #使用指定的Zi到mro里去寻找,调用其下一个类的方法
    方式3: Fu.fun(self);方法是在python2.x调用父类方法,python3.x不推荐使用

"""


class Animal:
    def __init__(self):
        print("Animal init")

    def run(self):
        print("animal run %s" % str(self))  # 子类调用的话,self就是子类


class Dog(Animal):
    def __init__(self):
        print("Dog init")
        super().__init__()
        # super(Dog, self).__init__()
        # Animal.__init__(self)

    def run(self):
        print("override Animal run")

    def dog_run(self):
        super().run()  # 调用父类方法--方式1
        super(Dog, self).run()  # 调用父类方法--方式2；
        Animal.run(self)  # 调用父类方法--方式3;    python2.x调用方式

        # Dog.dog_run(self)  # 递归调用子类自己的方法,会形成死循环
        print("dog_run executed ")


dog = Dog()  # 默认会调用父类__init__方法;如果子类重写了__init__,则调用子类的
dog.dog_run()
