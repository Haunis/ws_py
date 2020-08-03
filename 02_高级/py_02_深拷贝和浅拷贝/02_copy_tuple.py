"""
如果元组里的元素都是不可变的，则copy.copy()和copy.deepcopy()都是指向原来的元组
如果元组里的元素有可变的，则copy.copy()指向原来的元组，copy.deepcopy()会拷贝所有元素

"""
import copy

print("----------------1.元组里是不可变元素-------------------")
a = (11, 22)
b = copy.copy(a)  # 直接指向a,因为元组不可改变，增删改都不可进行，所以所幸直接指向原来的元组
c = copy.deepcopy(a)  # 也是直接指向a

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))  # 三个相等

print("----------------2.元组里是可变元素--------------------")
a = [11, 22]
b = [33, 44]
c = (a, b)
d = copy.copy(c)
e = copy.deepcopy(c)

print("id(c):", id(c))
print("id(d):", id(d))  # id(c)和id(d)相等，但是和id(e)不等
print("id(e):", id(e))
