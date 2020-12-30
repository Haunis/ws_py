"""
使用type()可以创建类
type("Dog", (), {"name": "tom", "age": 3})
    第一个参数:类名
    第二个参数:父类
    第三个参数:类属性
"""

MyClass = type("Dog", (), {"name": "tom", "age": 3})
print(type(MyClass))  # <class 'type'>

instance = MyClass()
help(MyClass)
