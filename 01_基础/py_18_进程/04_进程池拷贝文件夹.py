"""
需求:将test文件夹复制一份,新文件夹名为test_copy

所用api:
    os.listdir(".") #列出当前路径下所有文件
    os.mkdir("new_folder") #创建文件夹
    os.path.exists(dir_name) #判断文件或者文件夹是否存在
    os.remove(dir_name + "/" + file) #删除文件

主进程向子进程发信息使用:multiprocessing.Queue
子进程向主进程发信息使用:multiprocessing.Manager.Queue

print语句一行显示 print("\r xxxx")
"""
import os
import multiprocessing
import time


def copy_file(queue, src_dir_name, src_file_name, dst_dir_name):
    # print("pid:%d %s------>%s" % (os.getpid(), src_file_name, dst_dir_name))
    src_file = open(src_dir_name + "/" + src_file_name, "rb")  # src_file 是TextIOWrapper类型
    content = src_file.read()

    dst_file = open(dst_dir_name + "/" + src_file_name, "wb")
    dst_file.write(content)
    src_file.close()
    dst_file.close()

    time.sleep(0.1)  # 拷贝太快,暂停0.1s
    queue.put(src_file_name)


def create_dest_dir(dir_name):
    """
    如果已经存在该文件夹,先删除文件夹里的文件,再删除该文件夹
    """
    if os.path.exists(dir_name):
        print("已经存在:%s,删除中..." % dir_name)
        file_list = os.listdir(dir_name)
        for file in file_list:
            os.remove(dir_name + "/" + file)
        os.rmdir(dir_name)
        print("删除完成:%s,重新创建" % dir_name)
    os.mkdir(dir_name)


def main():
    # 1.遍历test文件夹
    src_dir = "./test"
    src_file_list = os.listdir(src_dir)

    # 2.创建目标文件夹
    dest_dir = "test_copy";
    create_dest_dir(dest_dir)

    # 3.开启进程池复制文件
    pool = multiprocessing.Pool(3)
    queue = multiprocessing.Manager().Queue()
    for file in src_file_list:  # file是str类型
        # print(type(file))
        pool.apply_async(copy_file, (queue, src_dir, file, dest_dir))

    pool.close()
    # pool.join()
    complete_num = 0
    src_file_num = len(src_file_list)
    while True:
        complete_file = queue.get()
        complete_num += 1
        # print("完成复制:%s" % complete_file)
        print("\r完成进度: %d %%" % (complete_num * 100 / src_file_num), end="")
        if complete_num == src_file_num:
            break;


if __name__ == "__main__":
    main()
