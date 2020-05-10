import os

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

final_str = ""
initial_str = save_list[0][0:-1]

i = 0
while i < len(save_list):
    final_str += initial_str + str(i) + "+"
    i += 1
final_str=final_str[0:-1]


print("final_str:%s" % final_str)
bat_cmd = "copy /b "+final_str+" new.ts"
print("bat_cmd:%s"%bat_cmd)

file = open("to_ts.bat", "w")
file.write(bat_cmd)
file.close()