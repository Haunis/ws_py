"""
int(x) :string转换为int类型
float(x) : string转换为float
str(x) : int 转string

"""

str = "123"
str_to_int = int(str)
print("str_to_int=%s,type(str_to_int)=%s"%(str_to_int,type(str_to_int)))

str = "123.000"
str_to_float = float(str)
print("str_to_float=%s, type(str_to_float):%s" % (str_to_float, type(str_to_float)))
