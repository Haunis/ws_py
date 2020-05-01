# continue关键字作用:一旦执行遇到continue会直接跳转至while条件,continue后面的代码不再执行

count = 10;
while count > 0:
    print("count = %d" % count)
    count = count - 1

# 1~100所有素数
i = 0;
while i <= 100:
    if i >= 2:
        j = 2
        isSu = True
        while j < i:
            if i % j == 0:
                isSu = False
                break;
            j += 1;
        if isSu:
            print("素数:%d" % i)
    i += 1
