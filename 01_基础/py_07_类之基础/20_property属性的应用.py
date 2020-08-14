#-*-coding:utf-8-*-

"""
property的一个小应用:
    访问私有属性的set和get方法,转换成直接访问属性
"""

class Women:
    def __init__(self):
        self.__age = 18
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if isinstance(age,int):
            self.__age =age
        else:
            print("age 不是整型")
    age = property(get_age,set_age)

def main():
    w = Women()
    # print(w._Women__age) #强制访问
    print(w.age)
    w.age = 22
    print(w.age)

if __name__=="__main__":
    main()


