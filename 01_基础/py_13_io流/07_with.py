# -*-coding:utf-8-*-

# with 会自动调用file.close()
# with 在以写的方式打开文件的时候经常用

with open("abc.txt","rb") as f:
    data = f.read()
    print("type(data):%s" % type(data))
    print(data)
    # f.write(b'21')
