import common_module  # 1.common_module.py 2.变量common_module指向common_module.py这个模块
from common_module import g_num
from common_module import num_list


def change_common():
    # common_module.g_num = 100 #可以更改common_module里g_num的值
    # common_module.num_list.append(100) #可以向common_module里的num_list添加载100

    global g_num
    g_num = 100  # 无法更改common_module里g_num的值; 此处g_num = 100的含义是本模块的变量g_num重新指向一个新的值100
    num_list.append(100)  # 可以更改common_module里的值，因为num_list指向的就是common_module里的num_list
