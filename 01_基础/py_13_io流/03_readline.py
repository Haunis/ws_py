"""
readline() #每次只读取一行

"""
file = open("abc.txt")

while True:
    text = file.readline()
    if text:  # 如果有读取的内容
        print(text, end="")
    else:
        break;

file.close()
