import random

"""
    导入random模块,生成随机整数
    result = random(a,b)# 生成的随机数在[a,b]之间,a必须小于等于b
"""
count = random.random()
print("count = %f" % count)
random_int = random.randint(1, 10)

print("random_int = %d" % random_int)

print("random.__file__:%s" % random.__file__)  # 记录random模块所在路径
print("random.__name__:%s" % random.__name__)  # 被导入时记录的是模块名,直接运行时是__main__
