"""
在子目录导入同级模块会报错,但是在根目录下就不会

"""

# import my_module as DogModule
from my_module import Dog  # 可以从模块里导入一部分

# dog = DogModule.Dog("旺财")
dog = Dog("旺财")
dog.run()
