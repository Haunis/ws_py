"""
zip(iterable,,,)
    将多个可迭代对象打包成一个列表，列表里的元素是元组，元组里每个元素是可迭代对象里的元素

如 li1 = ['a','b','c'],li2=[1,2,3]
zip(li1,li2)打包后变成

"""
li1 = ["a", "b", "c"]
li2 = [1, 2, 3]

zipped = zip(li1, li2)

print("\n----------1.list(zipped)----------")
print(list(zipped))  # [('a', 1), ('b', 2), ('c', 3)]

print("\n----------2.for循环迭代zipped里的元素----------")
zipped = zip(li1, li2)  # 上面的list(zipped)已经解包了，zipped里面没东西了，所以要重新创建一个包
for x, y in zipped:
    print(x, y)

print("\n----------3.zip(*zipped)解包----------")
zipped = zip(li1, li2)  # 需要重新创建一个包
a, b = zip(*zipped)
print(a)  # ('a', 'b', 'c')；解包出来的元素是元组
print(b)  # (1, 2, 3)
