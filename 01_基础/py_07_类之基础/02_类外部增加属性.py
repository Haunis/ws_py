"""
在python中可以在类的外部给对象增加属性,但这在开发中不常见,不推荐使用

"""


class Car:
    def run(self):
        print("car run,color=%s" % self.color)


car = Car()
car.color = "red"
print(car.color)
car.run()

car2 = car
print(car2.color)
