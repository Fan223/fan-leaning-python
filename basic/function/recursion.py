def fun1(num):
    if 1 == num:
        return 1
    else:
        return num * fun1(num - 1)


print(fun1(5))
