"""

和java里super稍有不同
java super:
    1.调用构造super()
    2.调用父类方法 super.fuFunction()

python super:
    super是一个特殊的类,super()就是使用super类创建的对象
    调用父类方法: super().fuFunction()

在python2.x调用父类方法:
    父类名.方法(self) 如:Fu.fun(self);  python3.x不推荐使用
"""


class Animal:
    def run(self):
        print("animal run")


class Dog(Animal):
    def dog_run(self):
        super().run()  # 调用父类方法
        Animal.run(self)  # python2.x调用方式
        # Dog.dog_run(self)  # 递归调用子类自己的方法,会形成死循环
        print("dog_run executed ")


dog = Dog()
dog.dog_run()
