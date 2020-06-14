def fun():
    print("fun called")


def main(target):
    target()


main(fun)
