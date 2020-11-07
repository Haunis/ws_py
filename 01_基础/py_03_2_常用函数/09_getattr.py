"""
getattr(obj,name):可以获取模块，对象里的属性或者方法
"""
import demo_module


class Cat(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name, "run")


def main():
    print("-------------1.获取模块里的函数----------------------")

    fun = getattr(demo_module, "say_hello")  # 获取指定模块里的函数名
    fun()

    print("\n-------------2.获取对象里的函数----------------------")
    cat = Cat("tom")
    fun = getattr(cat, "run")  # 获取指定模块里的函数名
    fun()


if __name__ == "__main__":
    main()
