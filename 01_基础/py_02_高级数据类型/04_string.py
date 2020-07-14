"""
字符串的定义: 双引号和单引号皆可
    1.单引号经常使用场景: '我的外号叫"哈哈"'
常用操作:
    1.str[index] #取字符串中某个索引的字符:
    2.len(str) #获取字符串str的长度
    3.str.count(substring) #获取字符串中substring出现的次数,如果str中不存在substring则返回0
    4.str.index(substring) #获取字符串str中首次出现substring的索引,如果str中不存在substring则报错
    5.str.find(substring) #和index(substring)功能一样,但str不存在substring时不会报错而是返回-1
    6.str.isspace() # 是否是空白字符 ,\r \t \n都是空白字符
    7.str.replace(old_str,new_str) #返回一个新字符串,而不对原字符串改变

注意事项：
    str是个类，注意不要使用str作变量

"""
print("-----------------------1.判断---------------------------")
my_str = "hello ,hello python"
print("str[0] : %s" % my_str[0])  # 获取某个索引的字符
print("len(str) : %s" % len(my_str))  # 获取字符串长度
print("str.count(\"hel\") : %s" % my_str.count("hel"))  # 获取字符串中某个子字符串出现的次数
print("str.index(\"hel\") : %s" % my_str.index("hel"))  # 获取字符串中首次出现子字符串的索引

# unicode字符串
# num = "⑴" #False True True
# num = "\u00b2" #False True True
num = "一千零一"  # 中文字符串
# 三者从上往下,判断的范围越来越大
print(num.isdecimal())  # False 开发时尽量选这个方法
print(num.isdigit())  # False 可以判断unicode数字字符
print(num.isnumeric())  # True可以判断中文字符

str_abc1 = "abcddddd"
str_abc2 = "abcddddd"
print("id(str_abc1)=%d" % id(str_abc1))
print("id(str_abc2)=%d" % id(str_abc2))
print("str_abc1==str_abc2 : %s" % (str_abc1 == str_abc2))  # True
print("str_abc1 is str_abc2 : %s" % (str_abc1 is str_abc2))  # True

print("-----------------------2.查找和替換---------------------------")
test_str = "hello,python"
print(test_str.find("ello"))  # 返回索引,不存在则返回-1
print(test_str.replace("python", "abc"))  # 返回新字符串,不会改变原有字符串
print("test_str = %s" % test_str)

print("-----------------------3.文本对齐---------------------------")
str_poem = [
    "静夜思",
    "窗前明月光",
    "疑是地上霜",
    "举头望明月",
    "低头思故乡"
]
for str_temp in str_poem:
    # print("|%s|"%str.ljust(10,"　"))#全角的空格就是中文空格
    # print("|%s|"%str.rjust(10,"　"))#宽度为10，文字居右对齐，不足是个的用空格补齐
    print("|%s|" % str_temp.center(10, "　"))

str2 = "name"

str3 = str2.center(10, "*")
print("str3 : %s" % str3)  # ***name***
print("len(str3):%d" % len(str3))  # 10

print("-----------------------4.去除空白字符---------------------------")
# str.strip() 去除字符串两边空白字符
# str.lstrip() 去除字符串左边空白字符
# str.rstrip() 去除字符串右边空白字符
test_str4 = "   haha \t"
print("test_str4:%s" % test_str4)
print("test_str4.trip():%s" % (test_str4.strip()))

print("-----------------------5.拆分和拼接字符串---------------------------")
origin_str = "静夜思\t 李白 \n 窗前明月光 疑似地上霜 \t 举头望明月 低头思故乡"
result_list = origin_str.split()  # 如果不传参数的话,默认使用所有空白空白符作为分隔符(\r,\t,\n 空格)
print("result_list : %s" % result_list)

result_join = "*".join(result_list)  # 使用*把列表中的元素拼接起来
print("result_join : %s" % result_join)
temp_str = "abcd" + str(123)  # 字符串拼接
print(temp_str)

print("-----------------------6.字符串切片---------------------------")
# 就是字符串的截取; 索引-1代表最后一个元素
str_num = "0123456789"
print("str_num[2:5] : %s" % str_num[2:5])  # 234, 包左不包右
print("str_num[2:] : %s" % str_num[2:])  # 2,到最后
print("str_num[:5] : %s" % str_num[:5])  # 01234, 从开始到索引5的字符串
print("str_num[:] : %s" % str_num[:])  # 完整字符串
print("str_num[:] : %s" % str_num[:])  # 完整字符串
print("str_num[::2] : %s" % str_num[::2])  # 02468,从开始到末尾,步长为2
print("str_num[2:-1] : %s" % str_num[2:-1])  # 2345678,从索引2到最后,不包含右边-1位置的字符串
print("str_num[-2:] : %s" % str_num[-2:])  # 89 末尾两个
print("str_num[-1::-1] : %s" % str_num[-1::-1])  # 9876543210;从最后一个到最开始,步长为-1,实现字符串倒置
print("str_num[::-1] : %s" % str_num[::-1])  # 9876543210;字符串倒置;可以省略开始和结尾

print("-----------------------7.遍历字符串---------------------------")
# 字符串也可以遍历...
str_origin = "abcde"
for temp in str_origin:
    print(temp)
