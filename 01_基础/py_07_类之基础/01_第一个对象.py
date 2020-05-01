"""
print()打印对象的引用,会打印出实体对象的内存地址(堆内存)
id()获取的也是对象的实体内存地址
print()和id()获取的内存地址是一样的

self: 就是java里的this

空对象:None ;判断某个对象是否是空对象  instance is None

身份运算符:
    is -- 判断两个对象内存地址是否一致
    is not -- 判断两个对象内存地址是否不一致

== : 判断两个对象的内容是否相等
    如 a = [1,2,3]; b = [1,2,3] ; ==判断为True, is判断为False

类是一个特殊的对象(类对象)
由类对象创建出来的对象就是实例对象;类对象只有一个,而实例对象可以有多个

实例:由类实实在在创建出来的对象

类的方法保存: 对象的实例方法是保存在类中;
    所有实例相同的方法共享(内存中只有一个方法),每个实例调用该方法时,把实例self传过去调用即可

"""


class Car:
    def run(self):  # 定义一个run()函数
        print("car run, self=", self)  # self指向的对象和调用处变量指向的对象是同一个对象


car = Car()  # 实例化Car这个类
car.run()

print("car=", car)  # 相当于打印一个元组
print("id(car)=%#x" % id(car))  # 实体对象的地址
