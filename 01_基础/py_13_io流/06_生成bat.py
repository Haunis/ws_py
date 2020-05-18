import os


# 生成bat脚本文件
def gene_bat(file_list):
    print("gene_bat called")
    final_str = ""
    initial_str = file_list[0][0:-1]

    i = 0
    while i < len(file_list):
        final_str += initial_str + str(i) + "+"
        i += 1
    final_str = final_str[0:-1]

    print("final_str:%s" % final_str)
    bat_cmd = "copy /b " + final_str + " new.ts"
    print("bat_cmd:%s" % bat_cmd)

    file = open("to_ts.bat", "w")
    file.write(bat_cmd)
    file.close()


# 直接合并文件
def gene_video_ts(file_list):
    initial_str = file_list[0][0:-1]
    i = 0
    while i < len(file_list):
        file_list[i] = initial_str + str(i)
        i += 1
    file_video = open("new.ts", "wb");  # 以二进制格式写文件
    for file_name in file_list:
        try:
            temp_file = open(file_name, "rb")  # 以二进制格式读文件
            content = temp_file.read()
            file_video.write(content)
            temp_file.close()
        except FileNotFoundError as error:
            print("file not found:%s" % error)
    file_video.close()


file_list = os.listdir(".")
save_list = []  # 保留当前目录下有用的文件
for file in file_list:
    if "." not in file:
        file_last_char = file[-1:]  # 文件名的最后一个字符
        if file_last_char.isdigit():  # 最后一个是数字才添加
            save_list.append(file)

print("save_list:%s" % save_list)
save_list.sort()
print("save_list:%s" % save_list)

# gene_bat(save_list)
gene_video_ts(save_list)
