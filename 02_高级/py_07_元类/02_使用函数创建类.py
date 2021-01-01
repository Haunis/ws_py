"""
函数里可以定义类
"""


def get_class(name):
    if name == "Cat":
        class Cat:
            def __init__(self):
                print("cat init")

        return Cat
    elif name == "Dog":
        class Dog:
            def __init__(self):
                print("dog init")

        return Dog


MyClass = get_class('Dog')
instance = MyClass()
