"""
二进制文件: 保存的内容不是直接给人阅读的,如音视频,图片文件等等
文本文件:可以使用文本编辑器查看的文件,本质上也是二进制文件

文件操作一般套路: 1.打开文件 → 2.读写文件 → 3.关闭文件

file.read()#读取文件全部内容

文件指针的概念：
	第一次打开文件，文件指针会指向文件开始的位置
	执行了read()后，文件指针会指向文件末尾。这个时候再使用read()就不会再读取任何内容了
"""
try:
    file = open("abc.txt")
    result = file.read()
    print(result)

    file.close()  # 记得关闭，否则会消耗系统资源，并且影响后续文件访问
except Exception as result:
    print(result)
