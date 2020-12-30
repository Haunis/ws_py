"""
int(x) :string转换为int类型
float(x) : string转换为float
str(x) : int 转string

"""

str = "123"
str_to_int = int(str)
print("str_to_int=%s,type(str_to_int)=%s" % (str_to_int, type(str_to_int)))

str = "123.000"
str_to_float = float(str)
print("str_to_float=%s, type(str_to_float):%s" % (str_to_float, type(str_to_float)))

int = 100
# int_to_str = str(int)#上面已经使用了str变量了
int_to_str = "%d" % int
print("int_to_str=%s, type(int_to_str):%s" % (int_to_str, type(int_to_str)))
