"""
操作系统标识内存时，最小寻址单位时字节
内存地址地址是连续的
"""

li = [1,2,3,4]
print(id(li))

print("li[0]:",id(li[0]))
li[0] = 3
print("li[0]:",id(li[0]))
print("li[2]:",id(li[2]))
