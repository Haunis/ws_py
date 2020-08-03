"""
字典的copy()方法也是浅拷贝
"""

a_dict = dict(name="张三", like=["music", "basketball"])
b_dict = a_dict.copy()  # 浅拷贝

print("id(a_dict[\"like\"]):", id(a_dict["like"]))
print("id(b_dict[\"like\"]):", id(b_dict["like"]))  # 相等

a_dict["like"].append("football")
print("a_dict:", a_dict)
print("b_dict:", b_dict)  # b_dict的内容也会跟着改变
