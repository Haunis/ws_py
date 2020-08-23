#! /usr/bin/python3
import os

success_msg = """

合并成功 ！！！！！

"""


def print_list(temp_list):
    for element in temp_list:
        print(element)


def sort_list(temp_list):
    min_len_element = temp_list[0]  # 设第一个元素长度最短
    for element in temp_list:
        if len(element) < len(min_len_element):
            min_len_element = element
    print("min_len_element:", min_len_element)
    min_len = len(min_len_element)

    max_len_element = temp_list[0]  # 设第一个元素长度最短
    for element in temp_list:
        if len(element) > len(max_len_element):
            max_len_element = element
    print("max_len_element:", max_len_element)
    max_len = len(max_len_element)

    from_index = 1  # 如果最小长度和最大长度不相等的话，取min_len-1到len的数字作为排序
    if min_len == max_len:  # 如果最小长度和最大长度相等，则取最后两位作为排序
        from_index = 2

    # 使用选择排序，将元素按角标从小到大排列
    for i in range(len(temp_list)):
        for j in range(i + 1, len(temp_list)):
            i_index = int(temp_list[i][min_len - from_index:])
            j_index = int(temp_list[j][min_len - from_index:])
            if i_index > j_index:
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]  # 交换两个元素


# 生成bat脚本文件
def gene_bat(file_list):
    final_str = ""
    for file_name in file_list:
        final_str += file_name + "+"

    final_str = final_str[0:-1]  # 去掉最后“+”
    bat_cmd = "copy /b " + final_str + " new.ts"
    print("bat_cmd:\n%s" % bat_cmd)

    file = open("to_ts.bat", "w")
    file.write(bat_cmd)
    file.close()


# 直接合并文件
def gene_video_ts(file_list):
    file_video = open("new.ts", "wb");  # 以二进制格式写文件
    for file_name in file_list:
        try:
            temp_file = open(file_name, "rb")  # 以二进制格式读文件
            print("open : %s" % file_name)
            content = temp_file.read()
            file_video.write(content)
            temp_file.close()
        except FileNotFoundError as error:
            print("file not found:%s" % error)
    file_video.close()


def main():
    file_list = os.listdir(".")
    save_list = []  # 保留当前目录下有用的文件
    for file in file_list:
        if "." not in file:
            file_last_char = file[-1:]  # 文件名的最后一个字符
            if file_last_char.isdigit():  # 最后一个是数字才添加
                save_list.append(file)

    print("-----------------before sort--------------------")
    print_list(save_list)
    # save_list.sort()#不好使
    sort_list(save_list)
    print("-----------------after sort--------------------")
    print_list(save_list)

    # gene_bat(save_list)
    gene_video_ts(save_list)
    print(success_msg)


if __name__ == "__main__":
    main()
