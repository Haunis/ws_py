import re


def main():
    while True:
        in_str = input("please input(end--stop):")
        if in_str == "end":
            break
        else:
            ret = re.match(r"^[a-zA-Z]*$", in_str)  # 是否是全英文
            print(ret)


if __name__ == "__main__":
    main()
