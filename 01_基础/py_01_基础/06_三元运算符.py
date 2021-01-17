"""
python里没有像c++，java里的三元表达式，不能忍。。没有怎么装b
c++,java里的三元表达式： a = a > b? a:b

不过python里可以有类似的表达： a = a if a>b else b

"""

a = 1
b = 2

ret = a if a > b else 100  # a>b成立则将a赋值给ret,否则将100赋值给ret

print(ret)  # 100
