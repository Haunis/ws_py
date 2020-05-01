"""
主要是高级数据类型 列表,元组,字典的使用演练

"""
from py_06_名片管理 import tools

"""
pass作用: 占位符if判断里若没有具体代码实现是使用pass,否则编译不过 
"""


def do_with_input():
    tools.print_introduction()
    input_str = input("请输入功能:")

    if input_str in [tools.FUN_NEW_CARD, tools.FUN_SHOW_ALL_CARD, tools.FUN_QUERY_CARD]:
        if input_str == tools.FUN_NEW_CARD:  # 新建名片
            tools.create_new_card()
        elif input_str == tools.FUN_SHOW_ALL_CARD:  # 显示全部
            tools.show_all_card()
        elif input_str == tools.FUN_QUERY_CARD:  # 查询名片
            tools.query_card()
        do_with_input()
        # pass
    elif input_str == tools.FUN_EXIT_SYSTEM:
        print("退出系统")
    else:
        print("请选择正确功能", end="\n")
        do_with_input()


do_with_input()
