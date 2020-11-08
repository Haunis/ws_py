"""
__class__:指向创建该实例的类对象
"""


class Demo:
    pass


d = Demo()
print(d)  # d指向实例对象
print(d.__class__)  # <class '__main__.Demo'> d.__class__指向类对象
