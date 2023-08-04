a = 10


def fun1():
    b = 10
    global c
    c = 20
    print(a, b, c)


fun1()
print(a)
# print(b)  # error
print(c)
