"""
判断某个数据类型a是否可以迭代： isinstance(a,Iterable)


"""
from collections import Iterable


def main():
    is_iterable = isinstance([1, 2, 3], Iterable)  # 是否是Iterable的实例(子类也行)
    print("is_iterable = %s" % is_iterable)


if __name__ == "__main__":
    main()
