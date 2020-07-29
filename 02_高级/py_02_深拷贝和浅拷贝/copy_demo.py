import copy

a = [11, 22]
b = [33, 44]
c = a

print("id(a)=%d" % id(a))
print("id(c)=%d" % id(c))  # a和c 指向同一块内存区域

print("\n----------copy----------------")
d = copy.copy(a)  # 浅拷贝
print("id(a):", id(a))
print("id(d):", id(d))  # d指向新的一块内存区域，但存储的变量指向a存储的变量
print("id(a[0]):", id(a[0]))
print("id(d[0]):", id(d[0]))  # d[0]指向a[0]存储的值

# a[0]=55
# print("a:",a)
# print("d:",d)#a[0]的值的改变，不会影响d[0]的值的改变

e = [a, b]
f = copy.copy(e)
print()
print("id(e)=%d" % id(e))
print("id(f)=%d" % id(f))  # 不同;f指向新的一块内存区域

print("id(e[0]):", id(e[0]))
print("id(f[0]):", id(f[0]))  # 相同################## 浅拷贝，列表里的变量指向原列表指向的变量

print("\n----------deepcopy----------------")
f = copy.deepcopy(a)  # 深拷贝
print("id(a):", id(a))
print("id(f):", id(f))  # 不同；f指向新的一块内存区域，但存储的变量指向a存储的变量

print("id(a[0]):", id(a[0]))
print("id(f[0]):", id(f[0]))  # 相同

print()
g = copy.deepcopy(e)
print("id(e):", id(e))
print("id(g):", id(g))  # 不同

print("id(e[0]):", id(e[0]))
print("id(g[0]):", id(g[0]))  # 不同##################；深拷贝，会将原列表里的内容拷贝到另外地方

print("id(e[0][0]):", id(e[0][0]))
print("id(g[0][0]):", id(g[0][0]))  # 两个相同，都是指向a[0]
