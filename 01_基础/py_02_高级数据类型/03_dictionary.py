#!/usr/bin/python3

"""
就是java里map
关于字典注意事项：
	1.数据是无序的(每次运行打印字典内容,顺序可能不一致)
	2.key是唯一的，只能使用字符串，数字或元组;只能使用不可变数据类型作为key
	3.值可以是任意数据类型
常用操作:
	1.取值 : dict[key]
	2.更新 : dict[key] = value
	3.删除 : dict.pop[key]
	4.获取长度 : len(dict)
	5.扩展字典 : dict.update(dict2);如果dict中存在dict2的键值对,则dict相应的value将会被更新
	6.清空 : dict.clear()
	7.遍历 : for key dict:
	8.列表里存字典

字典初始化：
    temp_dict = dict() #空字典
    temp_dict = dict(name="张三",age="22")
"""
dict_lee = {"name": "lee", "age": 18, "gender": True, "height": 178}
print("原始字典 dict_lee : %s" % dict_lee)

print("\n-----------------1.取值--------------------")
print("dict_lee[\"name\"] = %s" % dict_lee["name"])

print("\n-----------------2.增加/修改-----------------")
# 如果字典不存在key就向字典增加元素，存在则修改
print("添加 country:china, name:lee000")
dict_lee["country"] = "china"
dict_lee["name"] = "lee000"

print("添加后 dict_lee : %s" % dict_lee)

print("\n-----------------3.删除--------------------")
print("先使用pop删除 name")
dict_lee.pop("name")
print("删除后 dict_lee : %s" % dict_lee)
print("再使用 del 删除 age")
del dict_lee["age"]
print("删除后 dict_lee : %s" % dict_lee)

print("\n-----------------4.获取字典键值对数量--------------------")
print("len(dict_lee) : %d" % len(dict_lee))

print("\n-----------------5.扩展字典--------------------")
dict_lee2 = {"name": "lee2", "price": 18}
dict_lee.update(dict_lee2)
print("dict_lee : %s" % dict_lee)

print("\n-----------------6.清空字典--------------------")
dict_lee2.clear()
print("dict_lee2 : %s" % dict_lee2)

print("-----------------7.1 遍历--------------------")
dict_lee3 = dict_lee
for key in dict_lee3:
    print("%s : %s " % (key, dict_lee3[key]))

print("-----------------7.2 遍历--------------------")
for key, value in dict_lee3.items():
    print("%s : %s " % (key, value))

print("-----------------8.列表里存字典--------------------")
card_list = [{"name": "lee", "age": 20}, {"name": "wang", "age": 21}]
for card in card_list:
    print(card)
