"""
int(x) :string转换为int类型
float(x) : string转换为float
str(x) : int 转string

"""
print("--------------1.str转int----------------")
str_temp = "123"
str_to_int = int(str_temp)
print("ret=%s,type(ret):%s" % (str_to_int, type(str_to_int)))

print("\n--------------2.str转float----------------")
str_temp = "123.000"
ret = float(str_temp)
print("ret=%s, type(ret):%s" % (ret, type(ret)))

print("\n--------------3.int转str----------------")
int_temp = 100
ret = str(int_temp)
# ret = "%d" % int_temp
print("ret=%s, type(ret):%s" % (ret, type(ret)))
