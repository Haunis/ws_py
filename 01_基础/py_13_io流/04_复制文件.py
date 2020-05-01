file_origin = open("abc.txt")

file_dest = open("abc[副本]", "w")  # 只写方式打开

###################一次全写入############################
# text = file_origin.read()
# file_dest.write(text)

###################一行一行写############################
while True:
    text = file_origin.readline()
    if text:
        file_dest.write(text)  # 由于为关闭文件,所以文件指针还在末尾
    else:
        break

file_origin.close()
file_dest.close()
