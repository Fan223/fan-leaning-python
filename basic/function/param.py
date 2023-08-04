def fun1(a, b=10):
    print(a, b)


fun1(10)
fun1(10, 30)


def fun2(*args):
    print(args, type(args))


fun2(2)
fun2(2, 3, 4, 5)


def fun3(**kwargs):
    print(kwargs, type(kwargs))


fun3(a=10)
fun3(a=20, b=30, c=40)


def fun4(*args, **kwargs):
    pass
