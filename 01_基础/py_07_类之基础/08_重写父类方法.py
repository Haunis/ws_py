"""
重写父类方法:在子类中定义一个和父类相同的方法即可

"""


class Animal:
    def run(self):
        print("animal run")


class Dog(Animal):
    def run(self):
        print("dog run")


dog = Dog()
dog.run()
