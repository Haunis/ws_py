"""
数字类型：
    int(python2分长整型和短整型，python3不分，type(2**64)查看)
    float
    bool(非0即为真)
    complex

数字类型可以直接计算，如 int i = 3,bool flag = true;  i+flag = 4

非数字类型：字符串，列表，元组，字典
"""
age = 18  # int

height = 1.75  # 2.float

isMale = True  # 3.bool类型

name = "小明"  # 4.string

print("type(age):", type(age))  # 直接接在后面打印要接逗号

print("name=%s,age=%d, height=%2.f,isMale=%s" % (name, age, height, isMale))

print("age+isMale = %s" % (age + isMale))
print("age+isMale = %s" % (age + isMale))
