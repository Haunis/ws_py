class Car:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            print(k, v)


# car = Car('red') #error 必须传键值对的形式
car = Car(color='red')
