"""
在元类里指定表名,字段名
"""


# 主要功能:添加__mapings__,__table__类属性,删除uid,name,email,pwd类属性
class ModelMetaClass(type):
    """
    class_name: 需要创建的类名
    class_parents: 类的父类
    class_attr:类有哪些类属性,类方法,实例方法
    """

    def __new__(cls, class_name, class_parents, class_attr):
        __mappings__ = dict()
        print("class_attr:", class_attr)
        for k, v in class_attr.items():
            if isinstance(v, tuple):  # 只将uid,name,email,pwd添加进__mappings__里
                __mappings__[k] = v
        class_attr['__mappings__'] = __mappings__  # 添加__mappings__类属性
        class_attr['__table__'] = class_name  # 添加table类属性

        for k in __mappings__:  # 将类属性uid,email,pwd删除
            class_attr.pop(k)
        # return type(class_name, class_parents, class_attr)  # 创建类
        return type.__new__(cls, class_name, class_parents, class_attr)  # 创建类


class User(object, metaclass=ModelMetaClass):
    uid = ('f_uid', 'int unsigned')  # f_uid是保存在数据库中的字段名
    name = ('f_name', 'varchar(30)')
    email = ('f_email', 'varchar(30)')
    pwd = ('f_pwd', 'varchar(30)')

    # __mappings__ = {
    #     'uid': ('f_uid', 'int unsigned')
    #     'name': ('f_name', 'varchar(30)')
    #     'email': ('f_email', 'varchar(30)')
    #     'pwd ': ('f_pwd', 'varchar(30)')
    # }
    # __table__='User'
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        field = list()
        field_value = list()

        for k, v in self.__mappings__.items():
            field.append(v[0])  # 取出__mappings__里的字段
            field_value.append(getattr(self, k))  # 取出实例对象存储的字段对应的值

        print("filed:", field)
        print("field_value:", field_value)
        str_field = ','.join(field)
        # str_value = ','.join(field_value) #error,field_value里有int值
        str_value = ','.join([str(i) for i in field_value])

        sql = "insert into %s(%s)values(%s)" % (self.__table__, str_field, str_value)
        print("sql : ", sql)

        print("\n-------改进后--------\n")
        for index in range(len(field_value)):
            if isinstance(field_value[index], str):
                field_value[index] = "'%s'" % field_value[index]
        print("field_value:", field_value)
        str_value = ','.join([str(i) for i in field_value])
        sql = "insert into %s(%s)values(%s)" % (self.__table__, str_field, str_value)
        print("sql : ", sql)


if __name__ == "__main__":
    # print(User.__dict__)
    user = User(uid=1234, name='lee', email='123@126.com', pwd='pwd1111')
    user.save()
