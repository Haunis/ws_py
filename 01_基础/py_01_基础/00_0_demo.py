def sum_num(num):
    if num > 0:
        return num + sum_num(num - 1)
    elif num == 0:
        return 0


result = sum_num(100)
print(result)
