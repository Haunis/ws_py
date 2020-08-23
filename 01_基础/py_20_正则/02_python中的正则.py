"""
本demo演示python独有，而其他语言没有的
"""
import re

print("----------------------1.search---------------------")
# 不用从头开始匹配，匹配出第一个；返回Match对象
# search达到match的功能 re.search(r"^\d",xxx)
ret = re.search(r"\d+", "abcd9999abcd0000")
print(ret.group())

print("----------------------2.findall---------------------")
# 匹配所有，并返回列表;带括号()的话，有几个括号，返回的结果list里的每个元组就有几个元素
html_str = "<body><h1>abcd</h1></body>"
# ret = re.findall(r"<\w*>", html_str) #无括号;返回单纯list,list里是str
# ret = re.findall(r"(<\w*>)", html_str)#1括号;返回单纯list,list里是str
# ret = re.findall(r"<\w*>|(</\w*>)",html_str) ##1括号;返回list，list里只含有()里的内容
# ret = re.findall(r"(<\w*>)|(</\w*>)",html_str) #2个();list里是元组，元组里2元素
ret = re.findall(r"((<\w*>)|(</\w*>))", html_str)  # 3个()，list里是元组，元组里3个元素
print(ret)

print("----------------------3.sub---------------------")
# 将匹配到的字符串替换为制定的字符串,返回整个字符串；
# 支持函数调用
print("替换为指定字符串....")
temp_str = "a=1,b=2,c=3"
print("before：%s" % temp_str)
ret = re.sub(r"\d+", "999", temp_str)  # 返回字符串
print("after：%s" % temp_str)  # 原字符串并不会改变
print("ret：%s" % (ret))

print("sub支持函数调用....")


def increase(temp_match):
    print("in increase:", temp_match)
    result_str = temp_match.group()
    return str(int(result_str) + 100)


temp_str = "a=1,b=2,c=3"
ret = re.sub(r"\d+", increase, temp_str)
print("temp_str:%s" % temp_str)  # 原字符串并不会改变
print("ret：%s" % (ret))

print("----------------------4.split---------------------")
# 注意和string的split不同
# split返回列表
ret = re.split(r":| ", "a:18 b c")  # 按：或则空格切割
print(ret)
