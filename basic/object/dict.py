class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name):
        self.name = name


c = C('张三')
print(c.__dict__)
print(C.__dict__)
print(c.__class__)
print(C.__bases__)
print(C.__mro__)
print(A.__subclasses__())
