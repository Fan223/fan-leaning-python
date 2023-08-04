class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stuNo):
        super().__init__(name, age)
        self.stuNo = stuNo

    def info(self):
        super().info()
        print(self.stuNo)


stu = Student('张三', 19, 10001)
stu.info()
print(stu.stuNo)


class A:
    pass


class B:
    pass


class C(A, B):
    pass
