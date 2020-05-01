FUN_INTRODUCTION = """*********************************************
欢迎使用名片管理系统
名片内容:姓名,邮箱,手机号
1.新建名片
2.显示全部
3.查询名片

0.退出系统
*********************************************"""
FUN_NEW_CARD = "1"  # 新建
FUN_SHOW_ALL_CARD = "2"
FUN_QUERY_CARD = "3"
FUN_EXIT_SYSTEM = "0"
card_list = []


def print_introduction():
    print(FUN_INTRODUCTION, end="\n")


def create_new_card():
    name = input("请输入姓名:").strip()
    if is_exist_name(name):
        print("已经存在:%s" % name)
        return
    mail = input("请输入邮箱:").strip()
    phone = input("请输入手机号:").strip()
    # pass
    new_card = {"name": name, "mail": mail, "phone": phone}
    card_list.append(new_card)
    print("<<<<<新建名片完成>>>>>")
    print("新名片是: %s,%s,%s" % (name, mail, phone))


def show_all_card():
    if len(card_list) != 0:
        print("<<<<<全部名片如下:>>>>>")
        for card in card_list:
            # card_info = card["name"] + "\t\t" + card["mail"] + "\t\t" + card["phone"]
            print("%s\t\t%s\t\t%s" % (card["name"], card["mail"], card["phone"]))
    else:
        print("<<<<<<<系统无名片,请新建名片>>>>>>>")
    # pass


def query_card():
    if len(card_list) == 0:
        print("<<<<<<<系统无名片>>>>>>>")
        return;
    name = input("请输入要查询的姓名:").strip()
    if is_exist_name(name):
        card = find_card(name)
        # if card is None:
        #     print("<<<<<<<名片不存在>>>>>>>")
        #     return;
        print("<<<<<查找成功,结果如下:>>>>")
        print(card["name"] + "," + card["mail"] + "," + card["phone"])
        next_fun = input("请选择功能: 1-修改 ,2-删除 ,3-返回上级菜单:").strip()
        if next_fun == "1":
            new_card = modify_card(card)
            print("<<<<<修改完成>>>>> ")
            print("新名片为: %s\t\t%s\t\t%s" % (new_card["name"], new_card["mail"], new_card["phone"]))
        elif next_fun == "2":
            delete_card(name)
            print("<<<<<删除完成>>>>>")
        elif next_fun == "3":  # 返回上级菜单
            pass  # 啥也不用做,自动返回上级函数
        else:
            print("<<<<<请输入正确操作>>>>>")
        # pass
    else:
        print("<<<<<姓名不存在>>>>>")
    # pass


def is_exist_name(name):
    exist = False
    for card in card_list:
        if card["name"] == name:
            exist = True
            break;
    return exist


def find_card(name):
    for card in card_list:
        if card["name"] == name:
            return card
    return None


def modify_card(card_origin):
    """
    修改名片,并返回新名片
    :param name:  将要修改的名片
    :return: 新名片
    """
    for card in card_list:
        if card["name"] == card_origin["name"]:  # 找到了要修改的名片
            while True:
                input_name = input("请输入新名字:").strip()
                if is_exist_name(input_name):
                    print("名字已经存在,请输入新名字")
                else:
                    input_mail = input("请输入邮箱:").strip()
                    input_phone = input("请输入手机:").strip()

                    name = card_origin["name"] if len(input_name) == 0 else input_name
                    mail = card_origin["mail"] if len(input_mail) == 0 else input_mail
                    phone = card_origin["phone"] if len(input_phone) == 0 else input_phone

                    card["name"] = name
                    card["mail"] = mail
                    card["phone"] = phone
                    return card
    return None
    # pass


def delete_card(name):
    card = find_card(name)
    card_list.remove(card)  # 可以直接删除
